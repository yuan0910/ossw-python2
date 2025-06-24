class Lecture:
    def __init__(self, name='설정되지 않음', category='설정되지 않음', size=-1):
        self.__name=name
        self.__category=category
        self.__size=size
        self.__score=dict()

    #접근자 및 설정자
    def setName(self, name):
        self.__name=name

    def setCategory(self, category):
        self.__category=category

    def setSize(self, size):
        self.__size=size

    def getName(self):
        return self.__name
    
    def getCategory(self):
        return self.__category
    
    def getSize(self):
        return self.__size

    #과목 설정 출력 (setting=0)
    def showInfo(self):

        print('')
        print('>> 과목 설정 조회')
        print(f'과목 이름: {self.getName()}, 과목 구분: {self.getCategory()}, 과목 수강 인원: {self.getSize()}')
        print('-------------------------------------------------------------------')
        
        
    #과목 설정 변경 (setting=1)
    def setInitSettings(self):     
        
        print(' ')
        print('>> 현재 과목 설정')
        print(f'과목 이름: {self.getName()}, 과목 구분: {self.getCategory()}, 과목 수강 인원: {self.getSize()}')

        while True:
            print('')
            print('>> 과목 설정 변경')
            print('[NOTICE] 0. 취소, 1. 과목 이름 변경, 2. 과목 구분 변경, 3. 과목 수강 인원 변경')

            try:
                set = int(input())
            except ValueError:
                print('[ERROR] 숫자를 입력해주세요.')
                continue

            if set==0:
                print('')
                print('>> 0. 과목 설정 변경 취소')
                break

            elif set==1:
                print('')
                print('>> 1. 과목 이름 변경 선택')
                print(f'현재 과목 이름: {self.getName()}')
                print('변경할 이름을 입력해주세요 (취소시 0 입력)')
                name_set=input()
                if name_set=='0': continue
                else: self.setName(name_set)
            
            elif set==2:
                print('')
                print('>> 2. 과목 구분 변경 선택')
                print(f'현재 과목 구분: {self.getCategory()}')
                print('변경할 구분을 입력해주세요 (변경 취소시 0 입력)')
                category_set=input()
                if category_set=='0': continue
                else: self.setCategory(category_set)

            elif set==3:
                print('')
                print('>> 3. 과목 수강인원 변경 선택')
                print(f'현재 과목 수강인원: {self.getSize()}')
                print('변경할 수강 인원을 입력해주세요 (변경 취소시 0 입력)')
                
                size_set=input()
                if size_set=='0': continue

                try:
                    self.setSize(int(size_set))
                except ValueError:
                    print('[ERROR] 숫자를 입력해주세요.')
                    continue

            else:
                print('')
                print('[ERROR] 잘못된 코드 입력')

            print('')
            print('[NOTICE] 수정이 추가로 필요할시 1, 수정 종료시 이외의 키 입력')

            cont=input()
            if cont!='1': break

    #성적 입력 (setting=2)
    def settingScore(self):
        while True:
            std_temp=input('[NOTICE] 학번-성적 입력 // ex: 20250000-96 // (0 입력시 종료): ')

            if std_temp=='0': 
                print('>> 성적 입력 종료')
                break
            
            std_temp=std_temp.split('-')

            if len(std_temp)!=2:
                print('[ERROR] 잘못된 형식')
                continue
                
            else:
                try:
                    self.__score[std_temp[0]] = int(std_temp[1])
                except ValueError:
                    print('[ERROR] 성적은 숫자여야 합니다.')
        
        print(f'>> 현재 입력된 학생수 {len(self.__score)}')

    
    #성적 조회 (setting=3)
    def viewScore(self):
        while True:
            print('')
            print('[NOTICE] 1 성적 입력 현황 / 2 학번으로 검색 / 3 순위 조회 / 그외 입력시 종료')

            view_temp=input()

            if view_temp=='1':
                print('>> 1. 성적 입력 현황')
                print(f'{self.getSize()}명 중 {len(self.__score)}명 입력')

            elif view_temp=='2':
                print('>> 2. 학번으로 검색')
                std_id = input('[NOTICE] 학번을 입력하세요: ')
                
                if std_id in self.__score:
                    score = self.__score[std_id]
                    sorted_scores = sorted(self.__score.items(), key=lambda item: item[1], reverse=True)
                    rank = [sid for sid, _ in sorted_scores].index(std_id)+1
                    print(f'{std_id}의 성적: {score}점, 등수: {rank}위')
                else:
                    print('[ERROR] 해당 학번이 존재하지 않습니다.')


            elif view_temp=='3':
                sorted_scores=sorted(self.__score.items(), key=lambda item: item[1], reverse=True)
    
                #출력
                for rank, (std_id, score) in enumerate(sorted_scores, start=1):
                    print(f'{rank}. {std_id} - {score}점')
            else: 
                print('>> 성적 조회 종료')
                break

    
    #과목 관리 프로그램
    def manageLecture(self):
        
        print('-----------------------------------------------------------------------')
        print('### 과목 관리 시작 ###')
        print('')

        while True:

            print('')
            print('> 옵션 선택')
            print('[NOTICE] 0. 과목 설정 조회 / 1. 과목 설정 변경 / 2. 성적 입력 / 3. 성적 조회 / 그외 입력시 종료')
            print('')

            manage_code=input()
            if manage_code=='0': self.showInfo()
            elif manage_code=='1': self.setInitSettings()
            elif manage_code=='2': self.settingScore()
            elif manage_code=='3': self.viewScore()
            else: 
                print('과목 관리 종료')
                break
            
            print('')
            print('[NOTICE] 계속 관리하시겠습니까? (0. NO / Otherwise. YES)')
            
            cont=input()
            if cont=='0': break
