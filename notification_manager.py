from twilio.rest import Client


class NotificationManager:
    @classmethod
    def send_message(cls,body):
            account_sid = "ACbd8d735f387211d3a564912b17766ef9"
            auth_token = "a472c4fe7db3d97b9ff741905d31e42c"
            from_num = '+19164714592'
            to_num = "+918091782895"
            client = Client(account_sid, auth_token)
            body = body
            message = client.messages \
                .create(
                body=body,
                from_=from_num,
                to=to_num
            )
            print(message.status)