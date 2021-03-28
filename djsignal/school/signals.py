from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,pre_migrate,post_init,post_save,post_delete,post_migrate

# @receiver(user_logged_in,sender=User)
# def login_success(sender,request,user,**kwargs):
#     print("------------")
#     print("User Logged In:-Run Intro")
#     print("sender:-",sender)
#     print("Request:-",request)
#     print("User:-",user)
#     print("User password:-",user.password)
#     print(f'Kwargs:{kwargs}')
# # user_logged_in.connect(login_success,sender=User)



# @receiver(user_logged_out,sender=User)
# def log_out_success(sender,request,user,**kwargs):
#     print("------------")
#     print("User Logged In:-Outro bye bye..")
#     print("sender:-",sender)
#     print("Request:-",request)
#     print("User:-",user)
#     print(f'Kwargs:{kwargs}')
# # user_logged_out.connect(log_out_success,sender=User)


# # @receiver(user_login_failed,sender=User)
# def log_in_fail(sender,credentials,request,**kwargs):
#     print("------------------------------")
#     print("User login fail.-------------.")
#     print("Request:-",sender)
#     print("cred:-",credentials)
#     print("Request:-",request)
#     print(f'Kwargs:{kwargs}')
# user_login_failed.connect(log_in_fail,sender=User)


@receiver(pre_save,sender=User)
def at_pre_save(sender,instance,**kwargs):
    print("------------------------------")
    print("Pre Save Signals.-------------.")
    print("Request:-",sender)
    print("Request:-",instance)
    print(f'Kwargs:{kwargs}')
# pre_save.connect(at_pre_save,sender=User)


@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("------------------------------")
        print("Pre Save Signals.-------------.")
        print("Request:-",sender)
        print("Request:-",created)
        print("Request:-",instance)
        print(f'Kwargs:{kwargs}')
    else:
        print("------------------------------")
        print("Pre Save Signals.-------------.")
        print("Request:-",sender)
        print("Request:-",created)
        print("Request:-",instance)
        print(f'Kwargs:{kwargs}')
# pre_save.connect(at_pre_save,sender=User)

@receiver(pre_delete,sender=User)
def at_pre_delete(sender,instance,**kwargs):
        print("------------------------------")
        print("Pre delete Signals.-------------.")
        print("Request:-",sender)
        print("Request:-",instance)
        print(f'Kwargs:{kwargs}')
# pre_delete.connect(at_pre_delete,sender=User)

