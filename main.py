# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import time
import os

# remove useless collumn from a dataframe
def dataframe_remove_collumn(dataframe, keepCollumnArray):
    for element in dataframe:
        test_contain = False
        for collumn in keepCollumnArray:
            if(element == collumn):
                test_contain = True

        if(test_contain == False):
            dataframe = dataframe.drop([element], axis=1)
    return dataframe

# clean up dataframe
def dataframe_clean_up(dataframe, mainCollumnName):
    init_Col = 0
    for i in range(0, len(dataframe[mainCollumnName])):
        #print("hello")
        #print(dataframe[mainCollumnName][i])
        #print(dataframe[mainCollumnName][i] == dataframe[mainCollumnName][i])
        # check NaN value
        if(dataframe[mainCollumnName][i] == dataframe[mainCollumnName][i]):
            init_Col = i
            for element in dataframe:
                #print(element)
                try:
                    if(isNan(dataframe[element][init_Col])):
                        dataframe[element][init_Col] = [""]
                    else:
                        dataframe[element][init_Col] = [str(dataframe[element][init_Col])]
                except:
                    dataframe[element][init_Col] = [""]
                    pass
        else:
            for element in dataframe:
                #print(element)
                try:
                    #print(dataframe[element][init_Col])
                    array = dataframe[element][init_Col]
                    if(isNan(array)):
                        array = [""]
                    else:
                        if(isNan(dataframe[element][i])):
                            #print("do nothing")
                            array.append("")
                        else:
                            array.append(str(dataframe[element][i]))
                    dataframe[element][init_Col] = array
                except:
                    pass

    print(dataframe)
    dataframe = dataframe.dropna()



    return dataframe

def dataframe_treatment(dataframe, mainCollumnName, collumnArray):

    # remove useless collumn from a dataframe
    dataframe = dataframe_remove_collumn(dataframe, collumnArray)

    # clean up dataframe
    dataframe = dataframe_clean_up(dataframe, mainCollumnName)

    return dataframe


def isNan(value):
    if (value == value):
        return False
    return True

def create_folder(repertoire):
    #print(repertoire)
    if not os.path.exists(repertoire):
        os.makedirs(repertoire)
    while not os.path.exists(repertoire):
        time.sleep(0.5)

def valid_name(name):
    temp = name.replace(" * ", "__")
    temp = temp.replace(", ", "_")

    temp = temp.replace(" ", "_")
    temp = temp.replace("#", "")
    temp = temp.replace("-", "_")
    temp = temp.replace(":", "_")
    temp = temp.replace("?", "_")
    temp = temp.replace("!", "_")
    temp = temp.replace("/", "_")
    temp = temp.replace("\\", "_")
    temp = temp.replace("*", "_")
    temp = temp.replace("\"", "_")

    temp = temp.replace("(", "")
    temp = temp.replace(")", "")
    temp = temp.replace("@", "")
    temp = temp.replace("&", "")

    temp = temp.replace(".", "_")
    temp = temp.replace("\'", "")
    temp = temp.replace("’","")

    # _ become - i do that because of the url structure
    temp = temp.replace("_", "-")
    return temp

def create_Readme_feature(dataframe, path, element):
    print("feature : " + element[0])
    i_app = -1
    data_temp = dataframe_remove_collumn(dataframe, KeepCollumnApp)
    Author_end_insert = ""
    Description_insert = ""
    Acceptance_Criteria_insert = ""
    Array_userStories = []
    try:
        for element_dataframe in data_temp[mainCollumn]:
            i_app = i_app + 1
            if (element_dataframe[0] == element[0]):
                for key in Data_insert:
                    print("hello world")
                    temp_str = ""
                    res = remove_duplicate_from_list(data_temp[key][i_app])
                    print(key)
                    print(data_temp[key][i_app])
                    if (key == Author_end_insert_key):
                        for words in res:
                            # print(words)
                            if (words != ""):
                                temp_str = temp_str + str(words) + "<br>"
                        Author_end_insert = temp_str

                    if (key == Description_insert_key):
                        for words in res:
                                # print(words)
                            if (words != ""):
                                temp_str = temp_str + str(words).replace("\n", "<br>").replace("\r", "<br>") + " "
                                temp_str.replace("  ", "")
                        Description_insert = temp_str

                    if (key == Acceptance_Criteria_insert_key):
                        for words in res:
                            # print(words)
                            if (words != ""):
                                temp_str = temp_str + str(words).replace("\n", "<br>").replace("\r", "<br>") + " "
                                temp_str.replace("  ", "")
                        Acceptance_Criteria_insert = temp_str
                        print(Acceptance_Criteria_insert)
    except:
        pass

    if (os.path.isfile(path) == False):
        f = open(path, "w")
        f.writelines("# " + element[0] + "\n")
        f.writelines("___" + "\n")
        #f.writelines("\n")
        #f.writelines("<br>" + "\n")
        #f.writelines("\n")
        temp_path =  creation_path + "graph.md"
        #print(temp_path)
        w = open(temp_path, "r")

        for line in w.readlines():
            f.writelines(line.replace(replace_author,Author_end_insert).replace(replace_description,Description_insert).replace(replace_acceptance,Acceptance_Criteria_insert))

        w.close()


        i_app = -1
        data_temp = dataframe_remove_collumn(dataframe, KeepCollumnFeature)
        print("_________________")
        print(data_temp)
        data_temp_1 = dataframe_remove_collumn(dataframe, KeepCollumn)
        for x in ADD_CollumnFeature:
            data_temp[x]=""


        print(data_temp)

        temp_str = "|"
        temp_str1 = "|"
        for word in data_temp:
            temp_str = temp_str + word + "|"
            temp_str1 = temp_str1 + "---" + "|"
        f.writelines(temp_str.replace("||","|")+ "\n")
        f.writelines(temp_str1.replace("||","|")+ "\n")


        temp_str = ""
        j_app = -1
        try:
            for element_dataframe in data_temp_1[mainCollumn]:
                i_app = i_app + 1
                if(element_dataframe[0] == element[0]):
                    temp_str = "|"
                    for userStory_element in data_temp[userStoriesCollumn][i_app]:
                        j_app = j_app + 1
                        temp_str = "|"
                        for key in KeepCollumnFeature:
                            # res = remove_duplicate_from_list(data_temp[key][i_app])
                            res = data_temp[key][i_app]
                            try:
                                temp_str = temp_str + str(data_temp[key][i_app][j_app]).replace("\n", "<br>").replace("\r", "<br>") + " "
                                if(key==userStoriesCollumn):
                                    Array_userStories.append(str(data_temp[key][i_app][j_app]).replace("\n", "<br>").replace("\r", "<br>"))
                                    print(Array_userStories)
                            except:
                                temp_str = temp_str + " "
                                pass
                            temp_str.replace("  ", "")
                            temp_str.replace("  ", "")
                            temp_str = temp_str + " |"
                        f.writelines(temp_str + "\n")

        except:
            pass

        f.writelines("\n")
        f.writelines("<br>" + "\n")
        f.writelines("\n")
        f.writelines("___" + "\n")



        for x in Array_userStories:
            f.writelines("## " + x + "\n")
            f.writelines("### " + technical_explaination + "\n")
            temp_path = creation_path + "technical_explaination.md"
            # print(temp_path)
            w = open(temp_path, "r")

            for line in w.readlines():
                f.writelines(line)

            w.close()

            f.writelines("\n")
            f.writelines("<br>" + "\n")
            f.writelines("\n")

            f.writelines("### " + "Conclusion" + "\n")

            f.writelines("\n")
            f.writelines("<br>" + "\n")
            f.writelines("\n")
            f.writelines("___" + "\n")

        temp_path = creation_path + "style.html"
        # print(temp_path)
        w = open(temp_path, "r")

        for line in w.readlines():
            f.writelines(line)

        w.close()










        #f.write("hello feature")
        f.close()

def create_Readme_commit(dataframe, path):
    if (os.path.isfile(path) == False):
        f = open(path, "a")
        f.write("hello commit")
        f.close()

def create_Readme_app(dataframe, path, element):
    if(os.path.isfile(path)==False):
        f = open(path, "w")
        #print(path.replace("//","/").split("/")[2].replace("-"," "))
        appName_Title = filter_app_name(path.replace("//","/").split("/")[2].replace("-"," "))
        f.writelines('<link rel="stylesheet" href="./../style.css">' + "\n")
        f.writelines("\n")
        f.writelines("# " + appName_Title + "\n")
        f.writelines("___")
        f.writelines("\n")
        #f.writelines("<br>"+ "\n")
        #f.writelines("\n")
        f.writelines("\n")
        data_temp = dataframe_remove_collumn(dataframe, KeepCollumnApp)
        print(data_temp)
        temp_str = "|"
        temp_str1 = "|"
        f.writelines("## " + "Commit" + "\n")
        for word in data_temp:
            temp_str = temp_str + word + "|"
            temp_str1 = temp_str1 + "---" + "|"
        f.writelines(temp_str.replace("||","|")+ "\n")
        f.writelines(temp_str1.replace("||","|")+ "\n")
        f.close()
        create_Readme_app(dataframe, path, element)
    else:
        i_app = -1
        data_temp = dataframe_remove_collumn(dataframe, KeepCollumnApp)
        try:
            for element_dataframe in data_temp[mainCollumn]:
                i_app = i_app + 1
                if(element_dataframe[0] == element[0]):
                    temp_str = "|"
                    for key in KeepCollumnApp:
                        res = remove_duplicate_from_list(data_temp[key][i_app])
                        #print("res : "+ res)
                        #res = data_temp[key][i_app]
                        if(key == mainCollumn):
                            temp_str = temp_str + "[" + element[0] + "]" + "(./" + valid_name(Dynamics) + sep_sys + valid_name(element[0])+ sep_sys + file_name + ")"
                        else:
                            #for words in data_temp[key][i_app]:
                            for words in res:
                                #print(words)
                                if(words!=""):
                                    temp_str = temp_str + str(words).replace("\n", "<br>").replace("\r", "<br>") + " "
                                    temp_str.replace("  ", "")
                        temp_str.replace("  ", "")
                        temp_str = temp_str + " |"

            f = open(path, "a")
            f.writelines(temp_str + "\n")
            f.close()
        except:
            pass


def create_Readme_main(dataframe, path):
    w = open(path, "w")
    w.writelines("# " + title_doc + "\n")
    w.writelines("___" + "\n")
    w.writelines("<br>" + "\n")
    w.writelines("\n")
    for element in filter_name_app:
        #print("a")
        temp_path =  creation_path + parent_folder + sep_sys + valid_name(element[0]) + sep_sys + file_name
        #print(temp_path)
        f = open(temp_path, "r")

        for line in f.readlines():
            #print("a")
            #print(line)
            tp_str = "## " + "[" + element[0] + "]" + "(" + "./" + valid_name(element[0]) + sep_sys + file_name + ")"
            #print(tp_str)
            w.writelines(line.replace("./" + valid_name(Dynamics) + "/", "./" + valid_name(element[0]) + sep_sys + valid_name(Dynamics) + sep_sys ).replace("# ", "## ").replace("## " + element[0], tp_str).replace('<link rel="stylesheet" href="./../style.css">', ""))

        #w.writelines(temp_file + "\n")

        w.writelines("\n")
        w.writelines("<br>" + "\n")
        w.writelines("\n")
        f.close()


    #w.write("hello main")
    w.writelines('<link rel="stylesheet" href="./style.css">' + "\n")
    w.close()


def filter_app_name(value):
    # filter name app + mapping
    name_application = "default"
    for filters_app in filter_name_app:
        for filter in filters_app:
            if(filter.lower() in value.lower()):
                name_application = filters_app[0]

    return  name_application

def remove_duplicate_from_list(list):
    res = [i for n, i in enumerate(list) if i not in list[:n]]
    return res


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

title_doc = "Documentation"

# define path and file for input data and separator for CSV format
path = "./"
fileCSV = "data3.csv"
separator = ";"

# define wich collumn are relevant (need to use same order as your csv)
KeepCollumn = ["Title", "User Stories", "Tag", "Owner", "Priority", "Description", "Estimation", "Estimate", "Acceptance & Criteria"]
KeepCollumnApp = ["Title", "Priority", "Owner", "Estimate", "Description", "Acceptance & Criteria"] #main
KeepCollumnFeature = ["User Stories", "Owner", "Status", "Description User Stories"] #Doc feature
ADD_CollumnFeature = ["Status", "Description User Stories"]

mainCollumn = "Title"
userStoriesCollumn = "User Stories"

Data_insert = ["Acceptance & Criteria", "Description", "Owner" ]
Author_end_insert_key = "Owner"
Description_insert_key = "Description"
Acceptance_Criteria_insert_key = "Acceptance & Criteria"

replace_author = "Author_name_end"
replace_description = "Description_Insert"
replace_acceptance = "Acceptance&Criteria_insert"
technical_explaination = "Technical Explaination"


# path where the doc will be created
creation_path = "./"
parent_folder = "documentation"
sep_sys = "/"


# Treatment
df = pd.read_csv(path + fileCSV, delimiter=separator)
data = dataframe_treatment(df, mainCollumn, collumnArray=KeepCollumn)
data = data.reset_index()
data = dataframe_remove_collumn(data, keepCollumnArray=KeepCollumn)
print(data)

# structure
fixe = "Getting Started"
Dynamics = "Commit"

#file name
file_name = "Readme.md"

#filter name app
#if feature title contains 1 of the string inside an array then the name app will be the first string inside the array
#otherwise go on default
filter_name_app = [
["Application 1", "App_1"],
["Application 2", "App_2"],
["Application 3", "App_3"],
]

i = -1

path_main = creation_path + sep_sys + parent_folder + sep_sys
for element in data[mainCollumn]:
    i = i + 1

    # filter name app + mapping
    name_application = filter_app_name(str(element[0]).lower())

    path_base = creation_path + sep_sys + parent_folder + sep_sys + valid_name(name_application) + sep_sys + valid_name(Dynamics) + sep_sys + valid_name(element[0])
    create_folder(path_base)

    create_Readme_app(data, path_main + sep_sys + valid_name(name_application) + sep_sys + file_name, element)
    #create_Readme_commit(data, path_base + sep_sys + ".." + sep_sys + file_name)



    try:
        for userStory in data[userStoriesCollumn][i]:
            #print(str(userStory) + ":" + str(isNan(userStory)))
            if(isNan(userStory)):
                print("do nothing")
            else:
                # create_folder(path_base + sep_sys + valid_name(str(userStory)))
                # create_Readme_feature(data, path_base + sep_sys + valid_name(str(userStory)) + sep_sys + file_name)
                create_Readme_feature(data, path_base  + sep_sys + file_name, element)
    except:
        pass


create_Readme_main(data, path_main + file_name)

f = open(path_main + "style.css", "w")
style_css_path = creation_path + "style.css"
# print(temp_path)
w = open(style_css_path, "r")

for line in w.readlines():
    f.writelines(line)

w.close()
f.close()




