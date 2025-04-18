import pandas as pd
import re
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_prefix_pattern = r'^[A-Za-z][A-Za-z0-9_.-]*$'
    valid_email_mask = users['mail'].str.endswith('@leetcode.com') & \
                       users['mail'].str.extract(r'^(.*)@')[0].str.match(valid_prefix_pattern)
    valid_users = users[valid_email_mask]
    return valid_users