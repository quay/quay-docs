# Archatecture of Quay

Quay is make up of 3 core components and in highly avalable setups and additional object storeage component is part of the archatecture. 

The 3 core components are: 

    1. Database (MySQL or PostgresSQL)
       - Used by quay as it primary metadata and storage (not for image storage)
    2. Redis (key, value store)
       - Used for providing real time events and setup/install of Quay
    3. Quay as a Service
        - Internally (to the pod) their are several components

The 4th componnent of Quay is a storage component (where images are stored).

    - In public cloud enviornments (AWS, and Google), you should use the cloud providers object storage: Amazon S3, Google Cloud Storage
    - In private clouds an S3 or Swift compliant Object Store is needed: Ceph RADOS or OpenStack Swift

# Installing Quay

- https://coreos.com/quay-enterprise/docs/latest/initial-setup.html
- https://coreos.com/quay-enterprise/docs/latest/high-availability.html

## Pre-Requisites

- 1 VM / System with sufficent CPU, Memory and Storage
    - The System should be Registered and Subscribed to Red Hat. 
        - https://access.redhat.com/solutions/253273
    - 2vcpu, 8192MB RAM (roughly only 4029MB is needed for Quay, the rest is for overhead and CEPH), and ~10GBx3 of HDD Space
        - ~10GB HDD for OS (Red Hat, Fedora, Centos)
        - ~10GB+ HDD for docker storage
        - ~10GB+ HDD for Quay Local Storage (*optional*: You can install CEPH or other local storage options - requires more memory)
    - System should be configured to run [docker](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html-single/getting_started_with_containers/index)
- A valid (coreos) license is required to run Quay. Your license can be found on [Tectonic Accounts](https://account.tectonic.com/?_ga=2.89691474.855634678.1524488291-1499321380.1523978881). 
    - Please download or copy this license in Raw Format as a file named `license`.
    - This file will be placed in `/root/.docker/config.json` or `/home/USER/.docker/config.json` (which ever will be downloading the quay image).
 
## Installing a Local Test Instance

**Example inventory**: 
``` 
[hypervisor]
127.0.0.1 ansible_connection=local

[hypervisor:vars]
libvirt_bridges=[{'name': 'quaylab', 'forward': 'nat', 'bridge': 'virbr-900', 'domain': 'quaylab.lan', 'network': '192.168.254.0', 'broadcast': '192.168.254.255', 'ip_address': '192.168.254.254', 'ip_netmask': '255.255.255.0', 'dhcp_start': '192.168.254.1', 'dhcp_end': '192.168.254.253'}]
libvirt_pools=[{'virt-pool': { 'type': 'lvm', 'path': '/dev/nvme0n1p2' } }]

[lab:vars]
cloud_user_passwd="redhat"
resources={'vcpus': 2, 'ram': 8192, 'disks': [{'size': 10, 'pool': 'virt-pool'}, {'size': 10, 'pool': 'virt-pool'}], 'network': 'quaylab'}

[lab]
quay.quaylab.lan image_uri="http://porkchop.redhat.com/released/RHEL-7/7.5/Server/x86_64/images/rhel-guest-image-7.5-146.x86_64.qcow2" convert_to_lv_on_vg=virt-pool 
```
- **Note:** This uses KVM VM provisoning scrips: https://github.com/sferich888/fedora-minilab to provid the VM infastructure for a local lab. 

1. **Provision the Lab**
    - Follow the documenation for the ansible playbooks! This step can be skipped if you have other tools or method of get a requisit VM or system.

2. **Install Quay** Basic (Test)
	1. Manual 	
        1. **Register the System**
            - **Note:** [How to Register a RHEL system](https://access.redhat.com/solutions/253273)
            ```
            # subscription-manager register --username=<user_name> --password=<password>
            # subscription-manager refresh
            # subscription-manager list --available --matches '*IDK*'
            # subscription-manager attach --pool=<pool_id>
            # subscription-manager repos --disable="*"
            # subscription-manager repos \
                --enable="rhel-7-server-rpms" \
                --enable="rhel-7-server-extras-rpms" \
            ```
        1. **Setup Docker**
        	- **Note:** [Install and Setup Docker](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html-single/getting_started_with_containers/index)
        	```
            # sudo yum install docker
            
            # cat <<EOF > /etc/sysconfig/docker-storage-setup
            DEVS=/dev/vdb
            VG=docker-vg
            EOF
            # sudo docker-storage-setup
            
            # sudo systemctl enable docker
            # sudo systemctl start docker
            # sudo systemctl is-active docker
            ```
        1. **Install / Deploy a Database**
        	2. [MySQL](https://access.redhat.com/containers/#/registry.access.redhat.com/rhscl/mysql-57-rhel7)
                - Note: This DB is not persistant across reboots because a storage path is not provided. 
        	    ```
                # sudo docker \
                  run \
                  --detach \
                  --restart=always \
                  --env MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} \
                  --env MYSQL_USER=${MYSQL_USER} \
                  --env MYSQL_PASSWORD=${MYSQL_PASSWORD} \
                  --env MYSQL_DATABASE=${MYSQL_DATABASE} \
                  --name ${MYSQL_CONTAINER_NAME} \
                  --publish 3306:3306 \
                  - v /some/path:/var/lib/mysql/data:Z
                registry.access.redhat.com/rhscl/mysql-57-rhel7;
                ```
                
                - **TODO:** Test Connectivitiy (I have python for this)
            
        	3. [PostgresSQL](https://access.redhat.com/containers/?tab=overview#/registry.access.redhat.com/rhscl/postgresql-96-rhel7)
                ```
                $ sudo docker run -d --name postgresql_database -v /mnt:/var/lib/pgsql/data:Z -e POSTGRESQL_USER=test -e POSTGRESQL_PASSWORD=test -e POSTGRESQL_DATABASE=test -p 5432:5432 rhscl/postgresql-96-rhel7

                $ sudo docker exec -it postgresql_database /bin/bash -c 'echo "CREATE EXTENSION pg_trgm" | /opt/rh/rh-postgresql96/root/usr/bin/psql'
                CREATE EXTENSION

                ### Confirm that the Extension is Installed
                $ sudo docker exec -it postgresql_database /bin/bash -c 'echo "SELECT * FROM pg_extension" | /opt/rh/rh-postgresql96/root/usr/bin/psql'

                ```
                Notes: 
                Running Container: sudo docker run -d --name postgresql_database -v /mnt:/var/lib/pgsql/data:Z -e POSTGRESQL_USER=test -e POSTGRESQL_PASSWORD=test -e POSTGRESQL_DATABASE=test -p 5432:5432 rhscl/postgresql-96-rhel7
                Seeing What Extensions are Installed: `SELECT * FROM pg_extension;`
                Seeing what Extensions can be installed: `SELECT * FROM pg_available_extensions;`
                Install the Extension: `CREATE EXTENSION pg_trgm;`

                - **TODO:** Test Connectivitiy (need a better way)
            
        1. **Install / Deploy [Redis](https://access.redhat.com/containers/?tab=overview#/registry.access.redhat.com/rhscl/redis-32-rhel7)**
        ```
        # sudo docker run -d -p 6379:6379 registry.access.redhat.com/rhscl/redis-32-rhel7
        ```
        - **TODO:** Test Connectivitiy (need a better way)
            ```
            # yum install redis
            # redis-cli -h quay.quaylab.lan -p 6379 ping
            ```
        
        1. **Install / Deploy Quay**
        ```
        # mkdir -p /var/run/quay/config
      	### optional: if you don't choose to install an Object Store
     	# mkdir -p /var/run/quay/storage
  
        # sudo docker run --restart=always -p 443:443 -p 80:80 --privileged=true -v /var/run/quay/config:/conf/stack -v /var/run/quay/storage:/datastorage -d quay.io/coreos/quay:v2.9.1
        ```
        
        1. **Complete the Guided Setup**
      	    - visit: http://quay.quaylab.lan/setup
            - **Note:** The hostname of the lab can differ depending on how you deployed or configured the VM's
            1. Select DB Type
            2. Fill out the form and with DB details
            3. Fill out the form to create a SuperUser
            4. Fill out the configuration form > link to other sections on configuration. 
    
    1. Automated
    	1. Follow the [automation scripts]() to standalone install.
        - Run `ansible-playbook -i quay.inv_sample quaylab.yml -k` and fill in the prompts 
        - You then need to install ceph - if you want to use it
           - Note: https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/{producty}/html-single/installation_guide_for_red_hat_enterprise_linux/#installing-a-red-hat-ceph-storage-cluster 
           - You then need to create a USER: 
               - https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/{producty}/html/object_gateway_guide_for_red_hat_enterprise_linux/configuration#creating_a_literal_radosgw_literal_user_for_s3_access
           - You then need to create a bucket: (use the python script for this in the test directory). 
               - `python s3bucket_create.py` << Be sure to edit variables in this using data from user create. 

## Installing on OpenShift

- Use the quay-enterprise-template.yml template 
```
$ oc process -f quay-enterprise-template.yml -p AUTH_KEY=$(jq '.auths."quay.io".auth' config.json) | oc create -f -
```

## Installing a Production (Highly Avalable Instance) 
TODO: Do this - install template resouce give a fairly good example of whats needed here. 

Needs ~3 vm's (of similar sizes) + a Loadbalancer + Object Storage
 - HA DB Service is recommended see options for this below. 

In the Cloud you can use: 
AWS:    https://aws.amazon.com/rds/sqlserver/
        https://aws.amazon.com/rds/mysql/
        https://aws.amazon.com/rds/postgresql/

GOOGLE: https://cloud.google.com/sql/docs/
        https://cloud.google.com/sql/docs/mysql/high-availability
        https://cloud.google.com/sql/docs/postgres/high-availability

OpenStack: You could use Trove, if we Red Hat shipped or supported this (sadly we don't) 
        Red Hat seems ot have a partnership: https://docs.google.com/document/d/1veiYSTVckBU-oHEDQbimE-8sGOUMPXAUfkSjYOqP1v0/edit because trove is not something will ship with OSP
