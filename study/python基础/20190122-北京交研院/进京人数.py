"""
20181201-20190301
"""

num = 20190201
next_num = num+1
while next_num <= 20190228:
	day = "'" + str(num) + "'"
	next_day = "'" + str(next_num) + "'"

	sql = """
	insert overwrite table data_m.tmp_lxm_20190128_bj_jyy_cityod_result_one_02
	partition(day_id)
	select count(*),"""+day+"""
	from
	(select t1.mdn,t1.d_arrive_time,t1.d_city_id,t1.o_city_id
	from 
	(select mdn,d_arrive_time,o_city_id,
	(unix_timestamp(d_leave_time, 'yyyyMMddHHmmss') -
	unix_timestamp(o_arrive_time, 'yyyyMMddHHmmss')) / 3600 as duration
	,d_city_id
	from dws_m.dws_wdtb_city_od_msk_d
	where day_id in ("""+day + "," + next_day+ """)
	and d_city_id='81101'
	and o_city_id!='81101'
	and substr(d_arrive_time,1,8)="""+day+""" ) t1
	where t1.duration <= 48 
	group by t1.mdn,t12.d_arrive_time,t1.d_city_id,t1.o_city_id ) t2;"""

	print(sql)
	print()
	num +=1
	next_num +=1
