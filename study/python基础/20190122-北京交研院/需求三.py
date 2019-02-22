"""
全国城市出行分布（2019.1.28-2019.2.18），统计每日城际OD矩阵
"""

num = 20190201
next_num = num + 1
next_num_2 = num + 2
next_num_3 = num + 3

while next_num <= 20190218:
	day = "'" + str(num) + "'"
	next_day = "'" + str(next_num) + "'"
	next_day_2 = "'" + str(next_num_2) + "'"
	next_day_3 = "'" + str(next_num_3) + "'"

	sql = """
insert overwrite table data_m.tmp_lxm_20190128_bj_jyy_cityod_result_three
partition(day_id)
select t2.o_city_id,t2.d_city_id,count(*),"""+day+"""
from
(select t1.o_city_id,t1.d_city_id,t1.mdn,t1.o_leave_time
from
(select mdn,o_leave_time,o_city_name,d_city_name,
(unix_timestamp(d_arrive_time, 'yyyyMMddHHmmss') -
unix_timestamp(o_leave_time, 'yyyyMMddHHmmss')) / 3600 as duration
from dws_m.dws_wdtb_city_od_msk_d
where day_id in ("""+day+","+next_day+","+next_day_2+","+next_day_3+""")
and o_city_id != d_city_id
and substr(o_leave_time,1,8)="""+day+""" ) t1
where t1.duration <= 48
group by t1.o_city_id,t1.d_city_id,t1.mdn,t1.o_leave_time ) t2
group by t2.o_city_id,t2.d_city_id;"""

	print(sql)
	print()
	num += 1
	next_num += 1
	next_num_2 += 1
	next_num_3 += 1
