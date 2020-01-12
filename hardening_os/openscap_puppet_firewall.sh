#!/bin/bash

# Fix any open failures of oscap
oscap xccdf eval --remediate --fetch-remote-resources --profile xccdf_org.ssgproject.content_profile_pci-dss --report report.html /usr/share/xml/scap/ssg/content/ssg-centos7-ds.xml

# Check that all oscap issues are fixed
oscap xccdf eval --fetch-remote-resources --profile xccdf_org.ssgproject.content_profile_pci-dss  --report report.html /usr/share/xml/scap/ssg/content/ssg-centos7-ds.xml

# Setup Puppet repository: [check for latest version]
rpm -ivh https://yum.puppetlabs.com/el/7/products/x86_64/puppetlabs-release-22.0-2.noarch.rpm

# Install puppet master
yum install -y puppet-server


# Firewall Rules

# check default zone
sudo firewall-cmd --get-default-zone
# check zones used by network interfaces
sudo firewall-cmd --get-active-zones
# check all configurations for public zone
sudo firewall-cmd --zone=public --list-all
# switch zone to dmz
firewall-cmd --set-default-zone=dmz --permanent
firewall-cmd --zone=dmz --add-interface=enp0s3 --permanent

# Open puppet port for local clients
firewall-cmd --zone=internal --add-port=8140/tcp --permanent

# Reload rules
firewall-cmd --reload

# Start puppet master service
systemctl start puppetmaster.service


