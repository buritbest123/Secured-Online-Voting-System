import pandas as pd
from pathlib import Path
import hashlib
from encryption import encrypt_file, decrypt_file  # Importing encryption functions

path = Path("database")
encryption_key = 'test123'  # Define your encryption key here

def count_reset():
    decrypt_file(path / 'voterList.csv', encryption_key)
    voter_df = pd.read_csv(path / 'voterList.csv')
    voter_df['hasVoted'] = 0
    voter_df.to_csv(path / 'voterList.csv', index=False)
    encrypt_file(path / 'voterList.csv', encryption_key)

    decrypt_file(path / 'cand_list.csv', encryption_key)
    cand_df = pd.read_csv(path / 'cand_list.csv')
    cand_df['Vote Count'] = 0
    cand_df.to_csv(path / 'cand_list.csv', index=False)
    encrypt_file(path / 'cand_list.csv', encryption_key)

def reset_voter_list():
    decrypt_file(path / 'voterList.csv', encryption_key)
    df = pd.DataFrame(columns=['voter_id', 'Name', 'Gender', 'Zone', 'City', 'Passw', 'hasVoted'])
    df.to_csv(path / 'voterList.csv')
    encrypt_file(path / 'voterList.csv', encryption_key)

def reset_cand_list():
    decrypt_file(path / 'cand_list.csv', encryption_key)
    df = pd.DataFrame(columns=['Sign', 'Name', 'Vote Count'])
    df.to_csv(path / 'cand_list')
    encrypt_file(path / 'cand_list.csv', encryption_key)

def verify(vid, passw):
    decrypt_file(path / 'voterList.csv', encryption_key)
    voter_df = pd.read_csv(path / 'voterList.csv')
    for index, row in voter_df.iterrows():
        if row['voter_id'] == vid and row['Passw'] == passw:
            encrypt_file(path / 'voterList.csv', encryption_key)
            return True
    encrypt_file(path / 'voterList.csv', encryption_key)
    return False

def isEligible(vid):
    decrypt_file(path / 'voterList.csv', encryption_key)
    voter_df = pd.read_csv(path / 'voterList.csv')
    for index, row in voter_df.iterrows():
        if row['voter_id'] == vid and row['hasVoted'] == 0:
            encrypt_file(path / 'voterList.csv', encryption_key)
            return True
    encrypt_file(path / 'voterList.csv', encryption_key)
    return False

def vote_update(st, vid):
    if isEligible(vid):
        decrypt_file(path / 'cand_list.csv', encryption_key)
        cand_df = pd.read_csv(path / 'cand_list.csv')
        for index, row in cand_df.iterrows():
            if row['Sign'] == st:
                cand_df.at[index, 'Vote Count'] += 1

        cand_df.to_csv(path / 'cand_list.csv', index=False)
        encrypt_file(path / 'cand_list.csv', encryption_key)

        decrypt_file(path / 'voterList.csv', encryption_key)
        voter_df = pd.read_csv(path / 'voterList.csv')
        for index, row in voter_df.iterrows():
            if row['voter_id'] == vid:
                voter_df.at[index, 'hasVoted'] = 1

        voter_df.to_csv(path / 'voterList.csv', index=False)
        encrypt_file(path / 'voterList.csv', encryption_key)

        return True
    return False

def show_result():
    decrypt_file(path / 'cand_list.csv', encryption_key)
    cand_df = pd.read_csv(path / 'cand_list.csv')
    v_cnt = {}
    for index, row in cand_df.iterrows():
        v_cnt[row['Sign']] = row['Vote Count']
    encrypt_file(path / 'cand_list.csv', encryption_key)
    return v_cnt

# Hash function using sha256
def hash_password(password):
    password_bytes = password.encode('utf-8')
    hashed_password = hashlib.sha256(password_bytes).hexdigest()
    return hashed_password

def taking_data_voter(name, gender, zone, city, passw):
    decrypt_file(path / 'voterList.csv', encryption_key)
    voter_df = pd.read_csv(path / 'voterList.csv')
    row, col = voter_df.shape

    if row == 0:
        vid = 10001
        hashed_passw = hash_password(passw)
        df = pd.DataFrame({
            "voter_id": [vid],
            "Name": [name],
            "Gender": [gender],
            "Zone": [zone],
            "City": [city],
            "Passw": [hashed_passw],
            "hasVoted": [0],
        })
    else:
        vid = voter_df['voter_id'].iloc[-1] + 1
        hashed_passw = hash_password(passw)
        df1 = pd.DataFrame({
            "voter_id": [vid],
            "Name": [name],
            "Gender": [gender],
            "Zone": [zone],
            "City": [city],
            "Passw": [hashed_passw],
            "hasVoted": [0],
        })

        voter_df = pd.concat([voter_df, df1], ignore_index=True)

    voter_df.to_csv(path / 'voterList.csv', index=False)
    encrypt_file(path / 'voterList.csv', encryption_key)

    return vid
