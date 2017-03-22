
#! bin/sh
source /etc/profile
source ~./bashrc

hive -e "
add file hadoop习题1.py;
insert overwrite table database.table_name partition(partition_name＝'')
select product_no, lac_id, moment, start_time, user_id, country_id, staytime, city_id
from
	(from
		(select product_no, start_time, lac_id, staytime, moment, user_id, country_id, city_id
			from database.table_name_m 
			group by product_no
			order by product_no, start_time
			)
	reduce product_no, start_time, lac_id, staytime, moment, user_id, country_id, city_id using '/usr/bin/python hadoop习题1.py' as pre_product_no,pre_lac_id,pre_start_time,pre_staytime,pre_moment,pre_user_id,pre_country_id,pre_city_id
	)reduce_out;
">outcome.csv
