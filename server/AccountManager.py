from util import get, make_creds, URLOpenError, JSONDecodeError, \
                 InsufficientFunds
from util import settings
from database import get_username, get_balance, decrease_balance, increase_balance

class NotLoggedInError(Exception): pass

class AccountManager:
  NONE = 0
  TEST = 1
  SRND = 2
  GUEST = 3

  def logged_in(self):
    return bool(self.account_type)
  
  def __init__(self):
    self.account_type = AccountManager.NONE
    self.username = None
    self.rfid = None
    self.balance = None

  def log_in(self, rfid):
    if self.account_type == AccountManager.GUEST:
      return False
    if rfid == settings.TESTING_RFID:
      self.account_type = AccountManager.TEST
      self.username = settings.TESTING_USERNAME
      self.rfid = rfid
      self.balance = settings.TESTING_BALANCE
      return True
    else:
      self.account_type = AccountManager.SRND
      self.rfid = rfid
      self.username = get_username(rfid)
      self.balance = get_balance(rfid)
      return True

  def log_in_guest(self):
    self.account_type = AccountManager.GUEST
    self.username = "Guest"
    self.rfid = None
    self.balance = 0

  def log_out(self):
    self.account_type = AccountManager.NONE
    self.username = None
    self.rfid = None
    self.balance = None

  def deposit(self, amount):
    if not self.logged_in():
      raise NotLoggedInError()
    if self.account_type == AccountManager.SRND:
      increase_balance(self.rfid, amount);
      self.balance = get_balance();
    #If guest
    else:
      self.balance += amount

  def withdraw(self, amount, descript = None):
    if not self.logged_in():
      raise NotLoggedInError()
    if self.balance < amount:
      raise InsufficientFunds()
    if self.account_type == AccountManager.SRND:
      decrease_balance(self.rfid, amount);
      self.balance = get_balance();
    #If guest
    else:
      self.balance -= amount
