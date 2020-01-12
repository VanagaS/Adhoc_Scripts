#!/bin/bash

sudo mkswap -L volswap /dev/nvme1n1p1
sudo mkfs.xfs /dev/nvme1n1p2
sudo mkfs.xfs /dev/nvme1n1p3

if grep -q 'nvme1n1p1\|nvme1n1p2\|nvme1n1p3' /etc/fstab; then 
    echo "partition(s) already exist"
else

    sudo tee -a /etc/fstab <<EOF > /dev/null
/dev/nvme1n1p3 /tmp        xfs     loop,nosuid,noexec,nodev,rw  0   0
/dev/nvme1n1p2 /app_data   xfs     defaults,noatime             0   0
/dev/nvme1n1p1 swap        swap    defaults                     0   0
EOF

fi

sudo swapon -a
sudo swapon -s
sudo mount -a
