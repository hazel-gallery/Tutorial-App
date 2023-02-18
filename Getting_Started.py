import streamlit as st
from PIL import Image

st.title('Getting Started')
st.markdown('''
    Congratulations! You have successfully built the Tutorial app. 
    It's currently being hosted on our guest server, but you can 
    easily set it up on your own server after signing up and 
    following the tutorial. \n

    Before delving into the details, let's explain what just 
    happened behind the scenes. \n

    Generally, building a web application and configuring cloud 
    resources for it takes time. A typical application needs a 
    host machine, an operating system, databases, security, etc. 
    The bigger the application, the more complex the workflows 
    become. To simplify this process, we have wrapped the workflows 
    into a standard procedure. \n

    When selecting an app from the Gallery, a list of the 
    minimum required specs for cloud resources is displayed. 
    You may increase the specs to your perference.

''')
img_sys = Image.open('images/sys_min.jpg')
st.image(img_sys)

st.markdown('''
    Once finalized, Hazel sends the request to the cloud 
    provider (AWS in this case) to pull the resources and make 
    them ready for application building. All necessary dependencies 
    are then downloaded and installed to create the server environment. 
    After everything is set up, the server exposes an IP address 
    and the application becomes accessible as a web service.

''')

img_workflow = Image.open('images/workflow.png')
st.image(img_workflow)