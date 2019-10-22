from auth.authorize import auth


def test_authorize():
    print(
        auth(
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkZW1vIiwiaWF0IjoxNTcxNjc5OTY4LCJleHAiOjE1NzE3MjMxNjh9.hDZeoPrH6x4gyaERtj0-tREnuo9m1hqeKdDln-86-O0"
        )
    )
