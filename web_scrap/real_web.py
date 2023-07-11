from bs4 import BeautifulSoup
import requests
import time

import os

# Directory path
directory = "posts"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


print("Put some skill that you are not familiar with")
unfamiliar_skill = input("Enter some skills that you are not familiar with: ")
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    ).text

    soup = BeautifulSoup(html_text, "lxml")

    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text

        # get the latest job
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(
                " ", ""
            )
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")

            more_info = job.header.h2.a["href"]

            if unfamiliar_skill not in skills:

                with open(f"posts/{index}.txt", "w") as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f"File saved: {index}")


# Checks if scrpt is being executed as the main module.
# Ensures that the code is only run when the module is executed
if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
