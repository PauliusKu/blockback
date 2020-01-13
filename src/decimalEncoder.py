import sys
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return {
                "_type": "decimal",
                "value": str(obj)
            }
        return super(DecimalEncoder, self).default(obj)

