/*
初始化一个顺序表;
将若干奇偶数插入该顺序表并输出;
按照奇偶性调整顺序,奇数在前,偶数在后;
交换规则是若偶数在前则该位置上的与顺序表尾部的第一个奇数交换,依次交换直至所有元素位置都归位
*/
#include<stdio.h>
#include<malloc.h>
#define MaxSize 50

typedef int ElemType;
typedef struct
{
	ElemType data[MaxSize];
	int length;
} SqList;

//初始化线性表
void InitList(SqList *&L)
{
	L = (SqList *)malloc(sizeof(SqList));  //分配存放线性表的空间
	L->length = 0;                         //置空线性表长度为0
}

//销毁线性表
void DestroyList(SqList *L)
{
	free(L);
}

//判断线性表是否为空表
bool ListEmpty(SqList *L)
{
	return(L->length == 0);
}

//插入数据元素
bool ListInsert(SqList *&L, int i, ElemType e)
{
	int j;
	if (i<1 || i>L->length + 1)
		return false;                   //参数错误时返回false
	i--;                                //将顺序表逻辑序号转化为物理序号
	for (j = L->length; j > i; j--)            //将data[i]及后面元素后移一个位置
		L->data[j] = L->data[j - 1];
	L->data[i] = e;                       //插入元素e
	L->length++;                        //顺序表长度增1
	return true;                        //成功插入返回true
}

//输出线性表
void DispList(SqList *L)
{
	int i;
	if (ListEmpty(L)) return;
	for (i = 0; i < L->length; i++)
	{
		printf("%d ", L->data[i]);
	}
	printf("\n");
}

void move(SqList &L)
{
	int i = 0, j = L.length - 1;
	ElemType temp;
	while (i <= j)
	{
		while (L.data[i] % 2 == 1)
		{
			i++;
		}
		while (L.data[j] % 2 == 0)
		{
			j--;
		}
		if (i < j)
		{
			temp = L.data[i];
			L.data[i] = L.data[j];
			L.data[j] = temp;
		}
	}
}

void main()
{
	SqList *L;
	printf("顺序表的基本运算如下:\n");
	printf("   (1)初始化顺序表L\n");
	InitList(L);
	printf("   (2)此时线性表为：");
	ListInsert(L, 1, 2);
	ListInsert(L, 2, 3);
	ListInsert(L, 3, 6);
	ListInsert(L, 4, 8);
	ListInsert(L, 5, 7);
	ListInsert(L, 6, 1);
	ListInsert(L, 7, 5);
	ListInsert(L, 8, 9);
	DispList(L);

	printf("   (3)移动奇偶元素后线性表为:");
	move(*L);
	DispList(L);

	printf("   (4)释放顺序表L\n");
	DestroyList(L);

}
