def check_master(master_user, master_pass):
    if master_user == 'admin' and master_pass == 'password':
        return True
    
    return False