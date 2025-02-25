# From: https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/{producty}/html/object_gateway_guide_for_red_hat_enterprise_linux/configuration#creating_a_literal_radosgw_literal_user_for_s3_access
import boto
import boto.s3.connection

rdgw_hostname = "quay.quaylab.lan"
rdgw_port = 8880
##
# Fill this in after running: https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/{producty}/html/object_gateway_guide_for_red_hat_enterprise_linux/administration_cli#create_a_user
# $ radosgw-admin user create --uid=janedoe --display-name="Jane Doe" --email=jane@example.com
##
access_key = $access
secret_key = $secret
bucket = "quay_storage"

boto.config.add_section('s3')
boto.config.set('s3', 'use-sigv4', 'True')

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = rdgw_hostname,
        port = rdgw_port,
        is_secure=False,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

bucket = conn.create_bucket(bucket)
for bucket in conn.get_all_buckets():
	print "{name}\t{created}".format(
		name = bucket.name,
		created = bucket.creation_date,
)
