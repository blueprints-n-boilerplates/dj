from django.db.models import F, Q
from django.conf import settings

from twilio.rest import Client


def get_twilio_convo_base_url():
    """Builds the twilio conversation base url."""

    return f"https://conversations.twilio.com/v1/Services/{settings.TWILIO_CONVERSATIONS_SERVICE_SID}/Conversations/"


class TwilioBase:
    client = None

    def __init__(self, *args, **kwargs):
        self._auth_client()

    def _auth_client(self):
        # get credentials
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        # create client
        client = Client(account_sid, auth_token)
        self.client = client


class TwilioConversations(TwilioBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conversation_config = self._init_conversations_config()

    def _init_conversations_config(self):
        # https://www.twilio.com/docs/conversations/api/service-configuration-resource
        configuration = self.client.conversations.services(settings.TWILIO_CONVERSATIONS_SERVICE_SID)
        return configuration

    # Get

    def get_conversation(self, conversation_sid):
        return self.conversation_config.conversations(conversation_sid).fetch()

    def get_msgs(self, conversation_sid, limit=20):
        raw = self.get_conversation(conversation_sid).messages.list(limit=limit)
        clean = [{
            "body": msg.body,
            "author": msg.author,
            "attributes": msg.attributes,
            "media": msg.media,
            "index": msg.index,
            "delivery": msg.delivery
        } for msg in raw]
        return clean

    def get_msg(self, conversation_sid, msg_sid):
        return self.get_conversation(conversation_sid).messages(msg_sid).fetch()

    # Create

    def create_conversation(self, friendly_name=""):
        """Creates a twilio conversation resource."""

        conversation = self.conversation_config.conversations.create(
            friendly_name=friendly_name,
            messaging_service_sid=settings.TWILIO_MSGG_SERVICE_SID,
        )
        return conversation

    def add_msg(self, conversation_sid, author, body):
        # TODO:
        #   1. allow sending media

        _msg = self.get_conversation(conversation_sid).messages.create(
            author=author,  # email of the author
            body=body,
        )
        return _msg

    def start_conversation(self, participant, author, body, friendly_name=""):
        """
        Creates twilio conversation resource and conversation obj.
        Conversation Participant objs are then created and attached to the conversation resource and the obj.

        :param participant: Invited in the conversation <User obj>
        :param author: Initiator of the conversation <User obj>
        :param body: Starting message
        :param friendly_name: id of the author - id of the participant
        :return: Conversation obj
        """
        # 1. start twilio conversation
        # 2. create conversation obj
        # 3. create ConversationParticipant (intermediary model) obj for author and participant

        # twilio conversation resource
        _convo = self.create_conversation(friendly_name=friendly_name)

        # conversation obj
        convo, is_convo_created = Conversation.objects.get_or_create(
            sid=_convo.sid,
        )

        # conversation participant obj
        self.attach_participants(_convo, convo, [participant, author])

        _msg = self.add_msg(
            conversation_sid=_convo.sid,
            author=author.email,
            body=body
        )
        return convo

    # Update

    def update_msg(self, conversation_sid, msg_sid, new_body):
        return self.get_msg(conversation_sid, msg_sid).update(
            body=new_body
        )

    # Delete

    def delete_convo(self, conversation_sid):
        return self.get_conversation(conversation_sid).delete()

    def delete_msg(self, conversation_sid, msg_sid):
        return self.get_msg(conversation_sid, msg_sid).delete()

    # Other

    def attach_participants(self, _convo, convo, participants):
        """
        Creates Twilio Conversation Participant instances and attach the participants to the Twilio Conversation resource.
        Creates Conversation Participant objs and attach the participants to the Conversation obj.
        """

        for user in participants:
            # Twilio ConversationParticipant resource
            # attach participant to twilio conversation resource
            _p = _convo.participants.create(
                identity=user.email,
            )

            # Conversation Participant obj
            p, is_p1_created = ConversationParticipant.objects.get_or_create(
                conversation=convo,
                user=user
            )

        return convo
