class 계좌:
    def 개설(self, 이름, 잔고):
        self.이름 = 이름
        self.잔고 = 잔고

    def 출력(self):
        print("이름: ", self.이름)
        print("잔고: ", self.잔고)

계좌1 = 계좌()
계좌2 = 계좌()

계좌.개설(계좌1, "김철수", 500)
계좌.개설(계좌2, "이영희", 1000)

계좌.출력(계좌1)
계좌.출력(계좌2)