from auth.authorize import auth


def authorize(event, context):
    return auth(event, context)