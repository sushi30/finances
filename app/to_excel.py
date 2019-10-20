from app.models import FlowModel


def to_excel(id_):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            secrets["google_api"], scope
    )
    expense = FlowModel.get(id_).attribute_values



def handler(event, context):
    for record in event.get("Records"):
        ids = record["body"]
        for id_ in ids:
            to_excel(id_)
