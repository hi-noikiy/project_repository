# -*- coding: utf-8 -*-
# import os
# ziduan_dict={}
# with open(os.path.dirname(os.getcwd()) + '/util/ziduan_biao.txt', 'r')as code:
#     lines = code.readlines()
# for line in lines:
#     en=line.split(';')[0]
#     ch=map(lambda x:x.replace('\n','') ,line.split(';')[1].split(','))
#     ziduan_dict[en]=ch
# print ziduan_dict
def get_ziduan_dict():
    ziduan_dict={
     'construction_unit': ['建设单位'],
     'building_area': ['建筑面积'],
     'project_nature': ['项目性质','建设性质'],
     'construction_scale': ['建设规模', '建设内容及规模'],
     'accept_date_plan': ['拟受理日期'],
     'project_general_situation': ['项目概况'],
     'approval_number': ['批准文号'],
     'environment_assessment_form': ['环评形式'],
     'publicity_time': ['公示时间'],
     'publicity_time_limit': ['公示期限','公告时限'],
     'whether_accept': ['是否受理'],
     'examine_approve_unit': ['审批单位'],
     'industry_category': ['行业类别'],
     'huanping_agency': ['环评机构', '环评单位名称','环境影响评价机构','评价机构'],
     'yanshou_jiance_agency': ['监测单位','验收监测单位'],
     'download_link_huanping_report': ['环评报告下载链接'],
     'approval_publicity_start_date_plan': ['拟批准公示开始日期'],
     'public_announcement_start_date': ['公示公告开始日期'],
     'project_name': ['项目名称','建设单位/项目名称','建设单位／项目名称'],
     'agree_or_disagree': ['同意不同意字段'],
     'land_area': ['用地面积'],
     'public_feedback_opinion': ['公众反馈意见'],
     'huanbao_investment': ['环保投资'],
     'approval_publicity_end_date_plan': ['拟批准公示结束日期'],
     'file_name_huanping_report': ['环评报告文件名称','环境影响评价管理类别'],
     'investment_total': ['总投资'],
     'main_measure_environment_effect': ['主要环境影响及预防或者减轻不良环境影响的对策和措施'],
     'reply_date': ['批复日期'],
     'accept_time': ['受理时间', '受理日期'],
     'huanbao_measure': ['环境保护措施落实情况'],
     'project_address': ['建设地点']
     }
    return ziduan_dict
