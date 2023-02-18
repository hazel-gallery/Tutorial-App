import streamlit as st
from PIL import Image

st.title('Signing up')

st.markdown('''
    To sign up a Hazel account, you need to have an AWS access keys 
    already. The access keys are used to established the connection 
    between Hazel and your AWS account, which allows us to build applications
    using the cloud resources. Your access keys will be encypted for security
    purpose. Please follow the steps shown below:
''')

st.markdown('''
    :zero: This tutorial assumes you already have an AWS account.
    If you don't, please use [this link]({}). If the link does not work,
    please search "AWS Sign Up".  
'''.format('https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email')
)

st.text('')

st.markdown('''
    :one: After logging in your AWS account, in the top search bar, type in "IAM" and open the service
''')
keys_iam_img = Image.open('images/tutorial_keys_iam.png')
st.image(keys_iam_img)

st.text('')

st.markdown('''
    :two: After opening the service, you see the IAM dashboard. Choose :orange[**Users**]
    under the :orange[**Access management**] as pointed
''')
keys_dashboard_img = Image.open('images/tutorial_keys_dashboard.png')
st.image(keys_dashboard_img)     

st.text('')

st.markdown('''
    :three: Click :orange[Add users]. Fill in the user name you like and 
    Select AWS credential type as :orange[Access key - programmattic access].
    Click :orange[Next: Permissions]
''')
keys_users_img = Image.open('images/tutorial_keys_users.png')
st.image(keys_users_img)       

st.text('')

st.markdown('''
    :four: In the Set Permissions page, choose :orange[Attach existing policies directly].
    Type in :orange[AmazonEC2FullAccess] in the serach box and select the policy. Do it
    again for :orange[IAMFullAccess]. These two policies allow Hazel
    to create server instances and roles that help you connect to your server.
    Keep the default selection in :orange[Set permission boundary]. Click :orange[Next: tags]
''')
keys_permissions_img = Image.open('images/tutorial_keys_permissions.png')
st.image(keys_permissions_img)

st.text('')

st.markdown('''
    :five: You can skip the :orange[Add tags] page as it is optional.
    Click :orange[Next: Review]
''')

st.text('')

st.markdown('''
    :six: In the Review page, you should see the followings. Make sure 
    both :orange[AmazonEC2FullAccess] and :orange[IAMFullAccess] policies 
    are added. Click :orange[Create user]
''')
keys_review_img = Image.open('images/tutorial_keys_review.png')
st.image(keys_review_img)

st.text('')

st.markdown('''
    :seven: You should see a success page at this point with your 
    :orange[Access key ID] (access key) and 
    :orange[Secret access key] (secret key) 
    listed. Copy and paste them 
    to your notebook. You will need them to set up a Hazel account
''')
keys_success_img = Image.open('images/tutorial_keys_success.png')
st.image(keys_success_img)

st.text('')

st.markdown('''
    :eight: Go to the Account sign up page, enter the access key
    and screct key along with other information requested.
''')
keys_success_img = Image.open('images/tutorial_account_signup.png')
st.image(keys_success_img)
