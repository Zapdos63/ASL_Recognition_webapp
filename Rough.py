import os

mode = 'train'
directory = 'data/' + mode + '/'

count = dict(zero=len(os.listdir(directory + "/0")), one=len(os.listdir(directory + "/1")),
                 two=len(os.listdir(directory + "/2")), three=len(os.listdir(directory + "/3")),
                 four=len(os.listdir(directory + "/4")), five=len(os.listdir(directory + "/5")),
                 six=len(os.listdir(directory + "/6")), seven=len(os.listdir(directory + "/7")),
                 A=len(os.listdir(directory + "/A")), B=len(os.listdir(directory + "/B")),
                 C=len(os.listdir(directory + "/C")), D=len(os.listdir(directory + "/D")),
                 E=len(os.listdir(directory + "/E")), F=len(os.listdir(directory + "/F")),
                 G=len(os.listdir(directory + "/G")), H=len(os.listdir(directory + "/H")),
                 I=len(os.listdir(directory + "/I")), J=len(os.listdir(directory + "/J")),
                 K=len(os.listdir(directory + "/K")), L=len(os.listdir(directory + "/L")),
                 M=len(os.listdir(directory + "/M")), N=len(os.listdir(directory + "/N")),
                 O=len(os.listdir(directory + "/O")), P=len(os.listdir(directory + "/P")),
                 Q=len(os.listdir(directory + "/Q")), R=len(os.listdir(directory + "/R")),
                 S=len(os.listdir(directory + "/S")), T=len(os.listdir(directory + "/T")),
                 U=len(os.listdir(directory + "/U")), V=len(os.listdir(directory + "/V")),
                 W=len(os.listdir(directory + "/W")), X=len(os.listdir(directory + "/X")),
                 Y=len(os.listdir(directory + "/Y")), Z=len(os.listdir(directory + "/Z")))

no_of_images_train =

for image in count:
    no_of_images_train += image

print(no_of_images_train)