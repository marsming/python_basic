import random

# TODO:随机生成测验试卷文件

if __name__ == '__main__':
    #将测验数据保存到字典中
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
                'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort',
                'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
                'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City',
                'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord',
                'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
                'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    capitalsItems = list(capitals.items())
    # 生成35个测试文件.
    for quizNum in range(35):
        # 创建测试文件并打乱问题的次序.
        quizFile = open('../../datas/capitalsquiz%s.txt' % (quizNum + 1), 'w')
        answerKeyFile = open('../../datas/capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

        # 写出测试的题目.
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        # 打乱问题的次序.
        states = list(capitals.keys()) # 把所有的问题都列在一个列表中
        random.shuffle(states) # 将列表中的问题随机打乱

        # 每个试卷随机写入50个题.
        for questionNum in range(50):

            # 获取问题答案.
            correctAnswer = capitals[states[questionNum]]
            wrongAnswers = list(capitals.values()) # 得到一个完整的答案列表
            del wrongAnswers[wrongAnswers.index(correctAnswer)] # 删除正确答案
            wrongAnswers = random.sample(wrongAnswers, 3) # 将剩下3个答案随机打乱

            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions) # 将答案的顺序随机调整

            # 将问题和答案选项写在测试文件中.
            quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
            for i in range(4):
                quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

            # 写出一个文件的答案.
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()

