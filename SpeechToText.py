import speech_recognition as sr
import difflib
import re
import webbrowser


def compareFiles():
    print("4")
    first_file = "originalFile.txt"
    second_file = "textTospeech.txt"
    originalFileLines = open(first_file).read()
    originalFileLines = re.sub(' +', '\n', originalFileLines)
    originalFileLines = re.sub('\n+', '\n', originalFileLines)
    textReadFileLines = open(second_file).read()
    textReadFileLines = re.sub(' +', '\n', textReadFileLines)
    textReadFileLines = re.sub('\n+', '\n', textReadFileLines)
    a = open("originalFile.txt", 'w+')
    b = open("textTospeech.txt", 'w+')
    print("6")
    a.write(originalFileLines)
    b.write(textReadFileLines)
    a.close()
    b.close()
    originalFileLines = open(first_file).readlines()
    textReadFileLines = open(second_file).readlines()
    difference = difflib.HtmlDiff().make_file(originalFileLines, textReadFileLines, first_file, second_file)
    lines = difference.split("\n")

    count = 0
    editedDifference = ""
    for line in lines:
        if ("</body>" in line):
            editedDifference += '<h1>Count: {0}</h1>'.format(count)

        if (("<span class=\"diff_sub\">" in line) | ("<span class=\"diff_add\">" in line)):
            count = count + 1
        editedDifference += line + "\n"
    print(count)
    differenceReport = open('differenceReport.html', 'w')
    differenceReport.write(difference)
    differenceReport.close()

    differenceReportEdited = open('differenceReportEdited.html', 'w')
    differenceReportEdited.write(editedDifference)
    differenceReportEdited.close()
    webbrowser.open("differenceReportEdited.html")


r = sr.Recognizer()
with sr.Microphone() as source:
    print("SAY SOMETHING")
    audio = r.listen(source)
    print("Time Over,Thanks")
try:
    print("System predicts:" + r.recognize_google(audio))
    file1 = open("textTospeech.txt", "w")
    file1.write(r.recognize_google(audio))
    file1.close()
    compareFiles()

except:
    print("something went wrong");
