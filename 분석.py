import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import csv


row_color = []
intensity = []
white = []
red = []
green = []
blue = []
sky = []
pink = []
yellow = []

color = ['white', 'red', 'green', 'blue', 'sky', 'pink', 'yellow']

C_list= [[],[],[],[],[],[],[]]


def create_graph(data, x_values, title):
    gender = []
    values = []

    for item in data:
        parts = item.split()
        gender.append(parts[0])
        values.append(int(parts[1]))
        

    colors = ['blue' if g == 'm' else 'red' for g in gender]
    male_patch = mpatches.Patch(color='blue', label='Male')
    female_patch = mpatches.Patch(color='red', label='Female')

    plt.bar(x_values, values, color=colors)
    
    plt.xlabel('Color Intensity')
    plt.ylabel('Age')
    plt.title(title)


    # Add legends
    plt.legend(handles=[male_patch, female_patch])
    
    plt.show()


def main():
    f = open('분석.csv', encoding='utf-8-sig') 
    #['\ufeff강도&색', 이렇게 뜨는거 방지,파일 인코딩 표시
    data = csv.reader(f)
    header = next(data)
    
    for x in header:
        row_color.append(x)
    
    
    for row in data:
        intensity.append(row[0])
        white.append(row[1])
        C_list[0].append(row[1])
        red.append(row[2])
        C_list[1].append(row[2])
        green.append(row[3])
        C_list[2].append(row[3])
        blue.append(row[4])
        C_list[3].append(row[4])
        sky.append(row[5])
        C_list[4].append(row[5])
        pink.append(row[6])
        C_list[5].append(row[6])
        yellow.append(row[7])
        C_list[6].append(row[7])

    for i in range(0,7):
        create_graph(C_list[i], intensity ,color[i])

    f.close()
        
if __name__ == "__main__":
    main()