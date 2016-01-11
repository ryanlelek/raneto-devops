#!/bin/sh

# Reload IPTables Rules
/sbin/iptables-restore < /etc/network/firewall/iptables.config
