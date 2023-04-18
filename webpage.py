import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more imojis here:https://www.fx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="TIMMY TIMMY COMPUTERS",page_icon=":computer:",layout="wide")

def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
                return None
        return r.json()

#.......LOAD ASSETS.......
lottie_coding=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_q7bzwb0o.json")


#.....HEADER SECTIONS.....
st.subheader("Hi, I am Timmy :wave:")
st.title("A linux expert")
st.write("I am passionate about finding ways to make easier for a person to use linux ")
st.write("[Learn more>](https://t.me/timmytimmycomputers)")

#.....what i do ....
with st.container():
        st.write("___")
        left_column, right_column = st.columns(2)
        with left_column:
                st.header("WHAT I DO")
                st.write("##")
                st.write(
                   """
                        on my youtube channel i am creating tutorials for people who:\n
                       - are looking for way to leverage the power of linux in their day-to-day work.\n
                       - are  struggling with repetitive tasks in linux commands\n
                        If you are interesting to you,consider subcribing and turning on the notification.
                   """
                        )
        st.write("[YOUTUBE CHANNEL>](https://youtube.com)")
with right_column:
        st_lottie(lottie_coding,height=300,key="coding")

#......PROJECTS......
with st.container():
        st.write("___")
        st.header("my projects")
        st.write("##")
        st.subheader("EXCUTE C PROGRAMS USING LINUX")
        st.write(
            """
           Learn how to excute c programs using linux\n
           you can watch the video in my youtube channel.
            """
                )
st.markdown("[WATCH VIDEO...](https://youtu.be)")


with st.container():
        st.write("___")
        st.header("GET IN TOUCH WITH ME")
        st.write("##")

        #Documentation:https://formsubmit.co/!!!CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action = "https://formsubmit.co/nganga.16712@students.kyu.ac.ke@gmail.com"method="POST"/>
  <input type="hidden"name="_captcha" value="false">
                <input type="text"name="name"placeholder="your name"required>
                <input type="email"name="email"placeholder="your email"required>
                <textarea name="message"placeholder="your message here"required></textarea>
                <button type="submit">send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
        st.empty()


