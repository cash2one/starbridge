#这是一个分页方法
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
def list_page(request,list,display,after_range_num,bevor_range_num):
        # after_range_num = 3        #当前页前显示三页
        # bevor_range_num = 2        #当前页后显示两页
        paginator = Paginator(list,display)  #list，是传过来的查好的数据,display是一页展示多少条
        sum_page = paginator.num_pages #获得当前数据总共分页的页数

        try:
            page = int(request.GET.get('page'))
        except:
            page = 1
        try:
            list = paginator.page(page)
        except PageNotAnInteger:
            list = paginator.page(1)  # 页码不是整数,返回第一页
        except EmptyPage:
            list = paginator.page(paginator.num_pages)
        if page > after_range_num:
            page_range = paginator.page_range[page - after_range_num:page + bevor_range_num]  #用到的是range函数
            if page > sum_page - bevor_range_num:
                page_range=paginator.page_range[sum_page -after_range_num-bevor_range_num:page + sum_page] #这个if判断是为了，当点击最后两页的页数跳转时，页面只显示3个，如果加了判断的话，会显示五页
                if sum_page < after_range_num + bevor_range_num:   #这个if判断，是为了，当查询的时候，一共只有4页数据，如果点击第四页的话，前面的页数就没有了
                    page_range = paginator.page_range[0:sum_page]
        else:
            page_range = paginator.page_range[0:after_range_num + bevor_range_num]
        content={
            'list':list,
            'page_range':page_range
        }


        return content