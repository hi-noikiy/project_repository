# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XingzhengXukeHebeiItem(scrapy.Item):
    province_name = scrapy.Field()
    city_name = scrapy.Field()
    # title = scrapy.Field()
    # release_time = scrapy.Field()
    # department = scrapy.Field() #部门
    type = scrapy.Field() #填行政许可或行政处罚
    administrative_license_number = scrapy.Field() #行政许可决定文书文号/行政处罚决定文书文号
    project_name = scrapy.Field() #项目名称/处罚名称
    leibie_type = scrapy.Field() #审批类别
    licensed_content = scrapy.Field() #许可内容
    administrative_relative_name = scrapy.Field() #行政相对人名称
    social_credit_code = scrapy.Field() #行政相对人代码_1(统一社会信用代码)
    organization_code = scrapy.Field()  # 行政相对人代码_2(组织机构代码)
    business_registration_code = scrapy.Field()  # 行政相对人代码_3(工商登记码) /企业注册号
    tax_registration_number = scrapy.Field()  # 行政相对人代码_4(税务登记号)
    identification_number = scrapy.Field()  # 行政相对人代码_5 (居民身份证号)
    legal_representative = scrapy.Field()  # 法定代表人姓名/法定代表人/负责人
    approval_date = scrapy.Field()  # 许可决定日期
    license_deadline = scrapy.Field()  # 许可截止期
    licensing_authority = scrapy.Field()  # 许可机关
    current_state = scrapy.Field()  # 当前状态
    shuju_update_date = scrapy.Field()  # 数据更新时间
    comment = scrapy.Field()  # 备注
    download_link_attachment = scrapy.Field()
    attachment_path = scrapy.Field()
    url = scrapy.Field()

class XingzhengChufaHebeiItem(scrapy.Item):
    province_name = scrapy.Field()
    city_name = scrapy.Field()
    # title = scrapy.Field()
    # release_time = scrapy.Field()
    # department = scrapy.Field()  # 部门
    type = scrapy.Field()  # 行政许可或行政处罚
    administrative_license_number = scrapy.Field()  # 行政许可决定文书文号/行政处罚决定文书文号
    project_name = scrapy.Field()  # 项目名称/处罚名称
    chufa_typeone  = scrapy.Field()  # 处罚类型1
    chufa_typetwo  = scrapy.Field()  # 处罚类型2
    licensed_content = scrapy.Field()  # 处罚事由/违法违规行为
    punishment_basis = scrapy.Field()  # 处罚依据
    administrative_relative_name = scrapy.Field()  # 行政相对人名称
    social_credit_code = scrapy.Field()  # 行政相对人代码_1(统一社会信用代码)
    organization_code = scrapy.Field()  # 行政相对人代码_2(组织机构代码)
    business_registration_code = scrapy.Field()  # 行政相对人代码_3(工商登记码) /企业注册号
    tax_registration_number = scrapy.Field()  # 行政相对人代码_4(税务登记号)
    identification_number = scrapy.Field()  # 行政相对人代码_5 (居民身份证号)
    legal_representative = scrapy.Field()  # 法定代表人姓名/法定代表人/负责人
    approval_date = scrapy.Field()  # 处罚决定日期
    licensing_authority = scrapy.Field()  # 处罚机关
    local_code = scrapy.Field()  # 地方编码
    current_state = scrapy.Field()  # 当前状态
    shuju_update_date = scrapy.Field()  # 数据更新时间
    comment = scrapy.Field()  # 备注
    download_link_attachment = scrapy.Field()
    attachment_path = scrapy.Field()
    url = scrapy.Field()

item_dicts = {
    XingzhengXukeHebeiItem: 'xingzhengxuke_hebei_provinceLevel_all_xinyonghebei',
    XingzhengChufaHebeiItem: 'xingzhengchufa_hebei_provinceLevel_all_xinyonghebei'
}
