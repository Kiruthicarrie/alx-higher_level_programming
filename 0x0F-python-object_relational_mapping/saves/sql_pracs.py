# Use shift + Enter to run code line by line in python interactive console
# OR
# Select multi-lines and run using same key combination

python3.8  # starts python interactive console
# Import necessary modules
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# create engine and session
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# declarative base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

#--------------------------------------
User.__table__ 
Base.metadata.create_all(engine)
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
our_user
ed_user is our_user



session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')
    ])
ed_user.nickname = 'eddie'
session.dirty  # show all changes made to existing instances
session.new  # show all new instances
session.commit()  # save all changes made
# Lemme create myself
emmy = User(name='Emmanuel', fullname='Emmanuel Fasogba', nickname='emiwest')
session.add(emmy)  # .add adds it to pending state, ready to save to db
session.commit()  # .commit writes to db instance
users_list = session.query(User).all()
for item in users_list:
    print(item)

get_emmy = session.query(User).filter_by(nickname='emiwest').all()
get_emmy

#=======Rolling Back==========
emmy.nickname = 'imitor'
get_emmy = session.query(User).filter_by(nickname='imitor').all()
fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)
session.query(User).filter(User.name.in_(['Emmanuel', 'fakeuser'])).all()
session.rollback()
emmy.nickname
fake_user in session
# checking again
session.query(User).filter(User.name.in_(['Emmanuel', 'fakeuser'])).all()
# Now only pre-committed user 'Emmanuel' comes back, as
# uncommitted fake_user has been rolled back

# we can use Column.label to change / rename the column_name
for instance in session.query(User.nickname.label('username'),User.fullname.label('full_name')).all():
    print(f"{instance.username}==>{instance.full_name}")

# instead of dz
user=User
'''
for instance in session.query(user.nickname.label('username'),user.fullname.label('full_name')).all():
    print(f"{instance.username}==>{instance.full_name}")
'''
#use aliased
from sqlalchemy.orm import aliased
user_alias = aliased(User, name='user_alias')

for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)

# using limits and order by 
# using slices, we can limit outputs
for u in session.query(User).order_by(User.id)[0:2]:
    print(u)

# using filters
for name in session.query(User.name).filter(User.fullname=='Ed Jones'):
    print(name)


from sqlalchemy import tuple_
que=session.query(User).filter(
    tuple_(User.name, User.nickname).\
    in_([('ed', 'eddie'), ('wendy', 'windy')])
)
print(que)
[print(i) for i in que]

#========================== Table Relationships===================
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user =  relationship('User', back_populates='addresses')
    
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship(
    "Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)

# We are free to add Address objects on our User object.
# In this case we just assign a full list directly:
emmy.addresses = [Address(email_address='emmy@gmail.com'),
                  Address(email_address='emma@gmail.com')]

emmy.addresses

emmy_addr = session.query(Address).filter(Address.email_address=='emmy@gmail.com')
emmy_addr.all()

for u, a in session.query(User, Address).\
    filter(User.id==Address.user_id).\
    filter(Address.email_address=='emma@gmail.com').\
    all():
        print(u)
        print(a)
        
item = session.query(User).join(Address).\
    filter(Address.email_address=='emma@gmail.com').all()
print(item)

# sub-queries
from sqlalchemy.sql import func
stmt = session.query(Address.user_id, func.count('*').label('address_count')).group_by(Address.user_id).subquery()

print(stmt)

for u, count in session.query(User, stmt.c.address_count).outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id):
    print(u, count)

