from marshmallow import Schema, fields


class ProfessionalSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    project = fields.String()
    responsible = fields.String()
    work_experience = fields.Integer()
    level = fields.Decimal(as_string=True)
    hour_value = fields.Decimal(as_string=True)
    salary = fields.Decimal(as_string=True)
    current_work = fields.String()
    to_be_rated = fields.Boolean()
    data_created = fields.String()

    class Meta:
        ordered = True
