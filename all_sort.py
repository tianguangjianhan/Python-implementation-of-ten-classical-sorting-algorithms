class sort:
    def __init__(self):
        self.data=[1,5,6,4,2,9]
    def bubble_sort(self):
        '''
        ##冒泡排序
        时间复杂度：
        最好为O(n)数据为全正序但此时要加上交换标志,经过第一次n-1次的比较后交换标志不变号
        最差为O(n^2)数据为全逆序
        :return: data
        '''
        data=self.data[:]
        for i in range(len(data)):##一轮比较过后最大的数会变到最后去
            for j in range(1,len(data)-i):
                if data[j-1]>data[j]:
                    data[j],data[j-1]=data[j-1],data[j]
        return data
    def selection_sort(self):
        '''
        选择排序,每次选择最小的排到已排序数据的后面
        最好最坏时间复杂度都为O(n^2)
        :return: data
        '''
        data=self.data[:]
        for i in range(len(data)-1):
            min_index=i
            for j in range(i+1,len(data)-1):
                if data[j]<data[min_index]:
                    min_index=j
            data[i],data[min_index]=data[min_index],data[i]
        return data
    def quick_sort(self,data):
        '''
        快速排序,每次确定一个基准,大于基准的放右边,小于基准的放左边,然后左右边递归
        时间复杂度:
        一般的情况O(nlogn),logn是因为每次其实能确定的是基准base的位置,第一轮确定1个,第二轮确定2个
        第三轮确定4个....这些都是分开后都有数据存在的情况,这是要基准选的好
        最坏的情况O(n^2),当每次确定基准后左边或者右边有一个空数据的,则此时这一组只能确定一个base
        :param data
        :return:data
        '''
        if len(data)<=1:
            return data
        base = data[0]
        left=[data[i] for i in range(1,len(data)) if data[i]<=base]
        ##这里i和j要从1开始和它比较,不然和自身比较永远是相等,left永远递归不完
        right=[data[j]for j in range(1,len(data)) if data[j]>base]
        return self.quick_sort(left)+[base]+self.quick_sort(right)
    def merge_sort(self,data):
        '''
        归并排序,把数据不断二分成left和right两个部分,使用双指针比较左右部分的大小,再递归实现排序
        时间复杂度:
        最好最坏皆为O(nlogn),因为二分法后形成的二叉树的层数为logn,每次递归遍历n次
        :param data
        :return:data
        '''
        def merge(left,right):
            i=0
            j=0
            res=[]
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res+=left[i:]+right[j:]
            return res
        if len(data)<=1:
            return data
        mid=len(data)//2
        left=self.merge_sort(data[:mid])
        right=self.merge_sort(data[mid:])
        return merge(left,right)
    def heap_sort(self):
        '''
        堆排序
        大根堆:堆的完全二叉树结构中,父节点大于子节点
        小根堆:相反
        首先初始化大根堆,在构建的过程中从下往上构建,逆序遍历最后一层的非叶子结点,然后进入调整次序函数
        使用双指针定位左右子结点,用max_index定位最大值的结点初始化为该结点,如果左子结点大于max_index
        结点,则max_index=left.若右子结点大于max_index结点,则max_index=right.最后判断如果max_index
        与最开始的结点不相同则交换这两个的位置,并且递归调整max_index的堆.
        初始化完大根堆之后交换堆顶与堆末的位置然后对剩下的元素进行调整次序函数(写一个for循环,注意size要改变
        成剩下的元素的size)
        时间复杂度:
        最好最差都为nlogn,初始化大顶堆O(n),每层比较的次数是等比序列,循环交换顶末数据为n-1,新
        根节点下沉为logn,所以为O(n)+O(nlogn)=O(nlogn)
        :return:data
        '''
        def adjust_heap(data,i,size):
            left=2*i+1
            right=2*i+2
            max_index=i
            if left<size and data[left]>data[max_index]:
                max_index=left
            if right<size and data[right]>data[max_index]:
                max_index=right
            if max_index!=i:
                data[max_index],data[i]=data[i],data[max_index]
                adjust_heap(data,max_index,size)
        def built_heap(data):
            m=len(data)
            for i in range(m//2)[::-1]:
                adjust_heap(data,i,m)
        data=self.data[:]
        size=len(data)
        built_heap(data)
        for i in range(size)[::-1]:
            data[0],data[i]=data[i],data[0]
            adjust_heap(data,0,i)
        return data
    def insertion_sort(self):
        '''
        插入排序,默认第一个元素是已排好的序列,拿出第i个需要排序的数与之前的数比,比它大则这个数
        往后移,然后接着与之前的比,超出边界或者小于之后在这个停止的位置append这个数就行
        时间复杂度:
        最好情况O(n),完全有序只需要末尾比一次
        最坏情况O(n^2),完全逆序每次都要比
        :return:data
        '''
        data=self.data[:]
        for i in range(1,len(data)):
            temp=data[i]
            j=i-1
            while j>=0 and temp<data[j]:
                data[j+1]=data[j]
                j-=1
            data[j+1]=temp
        return data
    def shell_sort(self):
        '''
        希尔排序,将数据分成gap组,组内进行插入排序.然后gap=gap//2,接着组内插入排序.直到gap为0为止
        因为组内排过序了,所以再进行插入排序就快得多
        时间复杂度:
        平均O(n^1.3),取决于数据的分布和增量序列的好坏,O(n^2)最坏,O(n)最好
        优于直接插入排序
        :return:data
        '''
        data=self.data[:]
        m=len(data)
        gap=m//2
        while gap>0:
            for i in range(gap,m):
                for j in range(i,gap-1,-gap):
                    if data[i]<data[i-gap]:
                        data[i],data[i-gap]=data[i-gap],data[i]
                    else:
                        break
            gap=gap//2
        return data
    def counting_sort(self):
        '''
        计数排序,创建一个最大值-最小值范围的计数矩阵默认值为0,然后遍历整个数据为计数矩阵赋值
        然后按照计数矩阵的值把值赋到data数据里面,计数矩阵的顺序就是与最小值的偏移值.
        时间复杂度:
        最好最坏皆为O(n+k)
        :return: data
        '''
        data=self.data[:]
        maxdata=max(data)
        mindata=min(data)
        count=[0]*(maxdata-mindata+1)
        for i in data:
            count[i-mindata]+=1
        i=0
        for j in range(len(count)):
            while count[j]>0:
                data[i]=j+mindata
                count[j]-=1
                i+=1
        return data
    def bucket_sort(self):
        '''
        桶排序,预先设定好桶的size,把对应的数append到对应的桶里面,然后在桶里面用其他排序方法
        桶内排序完成后按照顺序将桶内的数据合并起来就是最后的结果
        时间复杂度:
        最好情况O(n),桶内排序使用O(nlogn)时间复杂度的排序算法,当桶的数量接近数据的数量时接近O(n)
        最坏情况O(n^2),都在一个桶内,桶内使用O(n^2)的排序算法
        平均情况O(n+k)
        :return:data
        '''
        data=self.data[:]
        scope=5
        maxdata=max(data)
        i=1
        while i*scope<=maxdata:
            i+=1
        bucket=[[]for f in range(i)]
        mindata=min(data)
        for j in data:
            bucket[(j-mindata)//scope].append(j)
        res=[]
        for m in bucket:
            m=self.quick_sort(m)
            res+=m
        return res
    def radix_sort(self):
        '''
        基数排序,从个位数开始循环到最大值的最大位数,是什么值就放到哪个桶里去,然后将所有的桶中的数据
        有序放出.接着计算十位、百位....
        时间复杂度:
        最好最坏都是O(n*k),k是最大位数.
        :return:data
        '''
        data=self.data
        mod=10
        div=1
        maxbit=len(str(max(data)))
        bucket = [[] for f in range(mod)]
        while maxbit:
            for i in data:
                bucket[i//div%mod].append(i)
            m=0
            for j in bucket:
                while j:
                    data[m]=j.pop(0)
                    m+=1
            maxbit-=1
            div*=10
        return data

a=sort()
print(a.bubble_sort())
print(a.selection_sort())
print(a.quick_sort(data=[1,5,6,4,2,9]))
print(a.merge_sort(data=[1,5,6,4,2,9]))
print(a.heap_sort())
print(a.insertion_sort())
print(a.shell_sort())
print(a.counting_sort())
print(a.bucket_sort())
print(a.radix_sort())
