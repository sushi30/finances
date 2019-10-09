from app.parse_expenses import handler

if __name__ == "__main__":
    handler(
        {
            "Records": [
                {
                    "s3": {
                        "bucket": {"name": "financeapp-inputfilesbucket-6zj9u7dmprhe"},
                        "object": {
                            "key": "leumicard/transaction-details_export_1563011498725.xlsx"
                        },
                    }
                }
            ]
        },
        None,
    )
