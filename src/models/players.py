from datetime import datetime


class Player:
    def __init__(self, first_name: str, last_name: str, birth_date: datetime.date, national_chess_identifier: str):
        self.first_name = first_name
        self.last_name = last_name
        if isinstance(birth_date, str):
            self.birth_date = datetime.strptime(birth_date, '%d/%m/%Y').date()
        else:
            self.birth_date = birth_date
        self.national_chess_identifier = national_chess_identifier

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return self.national_chess_identifier == other.national_chess_identifier

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date.strftime('%Y-%m-%d'),
            'national_chess_identifier': self.national_chess_identifier,
        }

    @classmethod
    def from_dict(cls, obj_dict):
        return cls(
            first_name=obj_dict['first_name'],
            last_name=obj_dict['last_name'],
            birth_date=datetime.strptime(obj_dict['birth_date'], '%Y-%m-%d').date(),
            national_chess_identifier=obj_dict['national_chess_identifier']
        )
