
from helpers import *


# MAIN
def main():
    interval = 30  # 30 seconds
    headers = {'Content-Type': 'application/json'}
    # cert = ('certificates/full_chain.pem', 'certificates/private_key.pem')

    # prod
    thing_id = 1
    token = "7b19e11c45adc6461822eaeed7f89d68844f35c701e04cb1bf86769693e7b7b5"
    url = "https://manjusapkota.com/phonehome/"

    # dev
    # thing_id = 1
    # token = "18c5f4d9c10729dc8f77280d69ac9d07d45193725cb6bc3fd998f7b736c91175"
    # url = "http://127.0.0.1:8000/phonehome/"
    try_registration = True
    while True:
        log("main():: Starting main loop ...")
        if 'THING_ID' in os.environ:
            thing_id = os.environ['THING_ID']
            log("main():: Found thing id in env variable: %s" % thing_id)
        if 'TOKEN' in os.environ:
            token = os.environ['TOKEN']
            log("main():: Found thing token in env variable %s" % token)
        if try_registration:
            log("main():: Try registration is True. So trying to do registration...")
            registration_success, registered_id = registration()
            if registration_success and registered_id:
                log("main():: New thing id from registration: %s" % registered_id)
                thing_id = registered_id
            if not registration_success:
                log("main():: Registration was not successful!")
                try_registration = False

        else:
            log("main():: Try registration is False. So not trying to do registration...")

        log("main():: thing id is :%s" % thing_id)
        message = get_info_for_phone_home(thing_id, token)
        phone_home_success, received_configs = phone_home(url, headers, message, cert)
        try_registration = True if phone_home_success else False
        if received_configs and received_configs["config"] is not None:
            results_of_policies_applied = apply_policies(received_configs)
            # log("result of applying config %s" % results_of_policies_applied)
            new_info = get_info_for_phone_home(thing_id, token)
            new_info["message"]["policy_execution_results"] = results_of_policies_applied
            phone_home(url, headers, new_info, cert)
        time.sleep(interval)


if __name__ == "__main__":
    main()

