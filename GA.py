# coding=utf-8
import random

# 遗传算法子
class GenAlg:
    @staticmethod
    def random():
        return random.randrange(0, 1)

    def __init__(self, popsize, MutRate, CrossRate, GenLenght, LeftPoint, RightPoint):

        # 代数的记数器
        self.generation = 0
        # 人口(种群)数量
        self.popsize = popsize
        # 基因突变的概率,一般介于0.05和0.3之间
        self.MuteRate = MutRate
        # 基因交叉的概率一般设为0.7
        self.CrossRate = CrossRate
        self.GenLength = GenLenght
        self.LeftPoint = LeftPoint
        self.RightPoint = RightPoint
        # 所有个体对应的适应性评分的总和
        self.totalFitness = 0
        self.generation = 0
        # 在所有个体当中最适应的个体的适应性评分
        self.bestFitness = 0.0
        # 在所有个体当中最不适应的个体的适应性评分
        self.worstFitness = 99999999
        # 所有个体的适应性评分的平均值
        self.averageFitness = 0
        # 最大变异步长
        self.maxPerturbation = 0.004
        # 最适应的个体在m_vecPop容器里面的索引号
        self.fittestGenome = None
        self.mutationRate = 0.05
        # 这个容器将储存每一个个体的染色体
        self.vecPop = []

        for i in range(1, popsize):
            pass

    def Reset(self):

        self.totalFitness = 0
        self.averageFitness = 0

    # 轮盘赌选择函数
    def CalculateBestWorstAvTot(self):

        for vec in self.vecPop:
            self.totalFitness += vec.fitness

            if vec.fitness >= self.bestFitness:
                self.fittestGenome = vec

            if vec.fitness <= self.worstFitness:
                self.worstFitness = vec.fitness

        self.averageFitness = self.totalFitness / self.popsize

    # 计算TotalFitness, BestFitness, WorstFitness, AverageFitness等变量
    def GetChromoRoulette(self):

        TheChosenOne = None

        Slice = (GenAlg.random()) * self.totalFitness
        FitnessSoFar = 0
        for vec in self.vecPop:
            FitnessSoFar += vec.fitness
            if FitnessSoFar >= Slice:
                TheChosenOne = vec
        return TheChosenOne

    # 基因变异函数
    def Mutate(self, chomos):

        for i in range(0, len(chomos)):
            if GenAlg.random() < self.mutationRate:
                chomos[i] += ((GenAlg.random() - 0.5) * self.maxPerturbation)

                if chomos[i] < self.LeftPoint:
                    chomos[i] = self.RightPoint
                elif chomos[i] > self.RightPoint:
                    chomos[i] = self.LeftPoint

    # 这函数产生新一代基因
    def Epoch(self):
        pass

    def GetBestFitness(self):
        return self.bestFitness

    def GetAverageFitness(self):
        return self.averageFitness

# 遗传运算引擎
class GenEngine:
    def report(self):
        pass

    def OnStartGenAlg(self):
        pass
