def increment_last_octet(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        return "Invalid IP address format"

    try:
        last_octet = int(parts[3])
        if last_octet < 255:
            last_octet += 1
            parts[3] = str(last_octet)
            return '.'.join(parts)
        else:
            return "Last octet already at maximum (255)"
    except ValueError:
        return "Invalid octet value"

    return (txt)
def make_route_base_IXR_big_md(data):
    txt = f"""
/configure card 1 mda 1 sync-e true
/configure card 1 mda 1 mda-type m24-sfp++8-sfp28+2-qsfp28
/configure log accounting-policy 27 admin-state enable
/configure log accounting-policy 27 description "MBH drop statistic collection"
/configure log accounting-policy 27 collection-interval 15
/configure log accounting-policy 27 record service-egress-packets
/configure log accounting-policy 27 destination file "27"
/configure log accounting-policy 28 admin-state enable
/configure log accounting-policy 28 description "MBH Drop collection"
/configure log accounting-policy 28 collection-interval 15
/configure log accounting-policy 28 record service-ingress-packets
/configure log accounting-policy 28 destination file "38"
/configure log log-events system event smScriptResult generate true
/configure log log-events system event smScriptException generate true
/configure log log-events vrtr event tmnxVRtrStaticRouteStatusChanged generate true
/configure log file "9" rollover 2880
/configure log file "9" retention 500
/configure log file "9" compact-flash-location primary cf3
/configure log file "27" description "SAP drop collection"
/configure log file "27" rollover 15
/configure log file "27" retention 4
/configure log file "27" compact-flash-location primary cf3
/configure log file "38" description "MBH"
/configure log file "38" rollover 15
/configure log file "38" retention 4
/configure log file "38" compact-flash-location primary cf3
/configure log file "95" description "Main Log File"
/configure log file "95" rollover 360
/configure log file "95" retention 72
/configure log file "95" compact-flash-location primary cf3
/configure log filter "1001" named-entry "10" description "Collect only events of major severity or higher"
/configure log filter "1001" named-entry "10" action forward
/configure log filter "1001" named-entry "10" match severity gte major
/configure log log-id "9" time-format local
/configure log log-id "9" source change true
/configure log log-id "9" destination file "9"
/configure log log-id "14" source debug true
/configure log {{ log - id "14" destination memory }}
/configure log log-id "20" source debug true
/configure log log-id "95" source main true
/configure log log-id "95" destination file "95"
/configure log log-id "98" source main true
/configure log log-id "98" source security true
/configure log log-id "98" source change true
/configure log log-id "98" destination snmp max-entries 1024
/configure log log-id "99" description "Default System Log"
/configure log log-id "99" source main true
/configure log log-id "99" destination memory max-entries 500
/configure log log-id "100" description "Default Serious Errors Log"
/configure log log-id "100" filter "1001"
/configure log log-id "100" source main true
/configure log log-id "100" destination memory max-entries 500
/configure log snmp-trap-group "98" description "5620sam"
/configure log snmp-trap-group "98" trap-target "10.100.16.132:162" address 10.100.16.132
/configure log snmp-trap-group "98" trap-target "10.100.16.132:162" version snmpv2c
/configure log snmp-trap-group "98" trap-target "10.100.16.132:162" notify-community "citrix"
/configure log snmp-trap-group "98" trap-target "10.100.20.68:162" address 10.100.20.68
/configure log snmp-trap-group "98" trap-target "10.100.20.68:162" version snmpv2c
/configure log snmp-trap-group "98" trap-target "10.100.20.68:162" notify-community "privatetrap98"
/configure log snmp-trap-group "98" trap-target "10.200.20.68:162" address 10.200.20.68
/configure log snmp-trap-group "98" trap-target "10.200.20.68:162" version snmpv2c
/configure log snmp-trap-group "98" trap-target "10.200.20.68:162" notify-community "privatetrap98"
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main1" address 10.200.20.68
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main1" notify-community "snmpv3user"
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main1" security-level privacy
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main2" address 10.100.20.68
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main2" notify-community "snmpv3user"
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main2" security-level privacy
/configure policy-options {{ community "service-lpbcks-IS0" member "48728:1110" }}
/configure policy-options {{ community "service-lpbcks-IS1" member "48728:1111" }}
/configure policy-options {{ community "service-lpbcks-IS2" member "48728:1112" }}
/configure policy-options {{ community "service-lpbcks-IS3" member "48728:1113" }}
/configure policy-options {{ community "service-lpbcks-IS4" member "48728:1114" }}
/configure policy-options {{ community "service-lpbcks-IS5" member "48728:1115" }}
/configure policy-options {{ community "service-lpbcks-IS6" member "48728:1116" }}
/configure policy-options {{ community "service-lpbcks-IS7" member "48728:1117" }}
/configure policy-options {{ community "service-lpbcks-IS8" member "48728:1118" }}
/configure policy-options {{ community "service-lpbcks-POC1" member "48728:11110" }}
/configure policy-options {{ prefix - list "lbl-bgp-lpbck" prefix {data["loopback"]} / 32 type exact }}
/configure policy-options prefix-list "only-lbl-bgp-lpbcks" prefix 192.168.64.0/20 type range start-length 32
/configure policy-options prefix-list "only-lbl-bgp-lpbcks" prefix 192.168.64.0/20 type range end-length 32
/configure policy-options policy-statement "export-to-POC2" entry 10 from prefix-list ["lbl-bgp-lpbck"]
/configure policy-options policy-statement "export-to-POC2" entry 10 action action-type accept
/configure policy-options policy-statement "export-to-POC2" entry 10 action origin igp
/configure policy-options policy-statement "export-to-POC2" entry 10 action community add ["service-lpbcks-IS1"]
/configure policy-options policy-statement "export-to-POC2" default-action action-type reject
/configure policy-options policy-statement "import-from-POC2" entry 10 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 10 from community name "service-lpbcks-IS{data["isis-a-area"]}"
/configure policy-options policy-statement "import-from-POC2" entry 10 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 10 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 20 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 20 from community name "service-lpbcks-POC1"
/configure policy-options policy-statement "import-from-POC2" entry 20 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 20 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 30 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 30 from community name "service-lpbcks-IS2"
/configure policy-options policy-statement "import-from-POC2" entry 30 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 30 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 40 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 40 from community name "service-lpbcks-IS3"
/configure policy-options policy-statement "import-from-POC2" entry 40 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 40 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 50 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 50 from community name "service-lpbcks-IS4"
/configure policy-options policy-statement "import-from-POC2" entry 50 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 50 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 60 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 60 from community name "service-lpbcks-IS5"
/configure policy-options policy-statement "import-from-POC2" entry 60 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 60 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 70 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 70 from community name "service-lpbcks-IS6"
/configure policy-options policy-statement "import-from-POC2" entry 70 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 70 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 80 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 80 from community name "service-lpbcks-IS7"
/configure policy-options policy-statement "import-from-POC2" entry 80 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 80 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 90 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 90 from community name "service-lpbcks-IS8"
/configure policy-options policy-statement "import-from-POC2" entry 90 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 90 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 100 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 100 from community name "service-lpbcks-IS0"
/configure policy-options policy-statement "import-from-POC2" entry 100 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 100 action action-type accept
/configure policy-options policy-statement "import-from-POC2" default-action action-type reject
/configure port {data["port-a1"]} admin-state enable
/configure port {data["port-a1"]} description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
/configure port {data["port-a1"]} ethernet collect-stats true
/configure port {data["port-a1"]} ethernet mtu 2102
/configure port {data["port-a1"]} ethernet ssm admin-state enable
/configure port {data["port-a1"]} ethernet egress port-qos-policy policy-name "NQ_VFQ_IXR_PORT_QOS"
/configure port {data["port-a1"]} ethernet network collect-stats true
/configure port {data["port-b1"]} admin-state enable
/configure port {data["port-b1"]} description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
/configure port {data["port-b1"]} ethernet collect-stats true
/configure port {data["port-b1"]} ethernet mtu 2102
/configure port {data["port-b1"]} ethernet ssm admin-state enable
/configure port {data["port-b1"]} ethernet egress port-qos-policy policy-name "NQ_VFQ_IXR_PORT_QOS"
/configure port {data["port-b1"]} ethernet network collect-stats true
/configure qos sap-ingress "102" description "Ingress for 2G full IP"
/configure qos sap-ingress "102" ingress-classification-policy "102"
/configure qos sap-ingress "102" policer 3 rate cir 100
/configure qos sap-ingress "102" policer 4 rate cir 100
/configure qos sap-ingress "102" policer 5 rate cir max
/configure qos sap-ingress "102" policer 6 rate cir max
/configure qos sap-ingress "102" policer 8 rate cir max
/configure qos sap-ingress "103" ingress-classification-policy "103"
/configure qos sap-ingress "103" policer 3 rate cir 100
/configure qos sap-ingress "103" policer 4 rate cir 100
/configure qos sap-ingress "103" policer 5 rate cir max
/configure qos sap-ingress "103" policer 6 rate cir max
/configure qos sap-ingress "103" policer 8 rate cir max
/configure qos sap-ingress "104" description "4G LTE SAP Ingress policy"
/configure qos sap-ingress "104" ingress-classification-policy "104"
/configure qos sap-ingress "104" policer 1 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 1 mbs 12800000
/configure qos sap-ingress "104" policer 1 cbs 6400000
/configure qos sap-ingress "104" policer 2 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 2 mbs 12800000
/configure qos sap-ingress "104" policer 2 cbs 6400000
/configure qos sap-ingress "104" policer 3 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 4 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 5 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 5 rate cir max
/configure qos sap-ingress "104" policer 6 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 6 rate cir max
/configure qos sap-ingress "104" policer 7 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 7 rate cir max
/configure qos sap-ingress "104" policer 8 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 8 rate cir max
/configure qos sap-ingress "110" description "Real Time VBR QOS"
/configure qos sap-ingress "110" ingress-classification-policy "110"
/configure qos sap-ingress "120" description "Signalling QOS"
/configure qos sap-ingress "120" ingress-classification-policy "120"
/configure qos sap-ingress "120" policer 7 rate cir max
/configure qos sap-ingress "130" description "Critical Data OP QOS"
/configure qos sap-ingress "130" ingress-classification-policy "130"
/configure qos sap-ingress "140" description "Critical Data IP QOS"
/configure qos sap-ingress "140" ingress-classification-policy "140"
/configure qos sap-ingress "150" description "Real Time CBR QOS"
/configure qos sap-ingress "150" ingress-classification-policy "150"
/configure qos sap-ingress "150" policer 6 rate cir max
/configure qos sap-ingress "160" description "Network Control QOS"
/configure qos sap-ingress "160" ingress-classification-policy "160"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" description "IXR Network QoS"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 1 queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 2 queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 3 queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 3 scheduler-mode wfq percent-rate cir 80.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 4 queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 4 scheduler-mode wfq percent-rate cir 80.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 5 queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 5 scheduler-mode wfq percent-rate pir 10.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 5 scheduler-mode wfq percent-rate cir 10.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 6 queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 6 scheduler-mode wfq percent-rate cir 100.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 7 queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 7 scheduler-mode wfq percent-rate cir 10.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 8 queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 8 scheduler-mode wfq percent-rate cir 20.0
/configure qos vlan-qos-policy "102" description "Egress for 2G full IP"
/configure qos vlan-qos-policy "102" queue 5 percent-rate cir 100.0
/configure qos vlan-qos-policy "102" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "102" queue 8 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" description "User Traffic delivered to full IP nodeB"
/configure qos vlan-qos-policy "103" queue 3 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 4 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 5 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 6 queue-forwarding-type expedite-hi
/configure qos vlan-qos-policy "103" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 8 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" description "4G LTE SAP Egress policy"
/configure qos vlan-qos-policy "104" queue 1 queue-mgmt "QM_104_12500"
/configure qos vlan-qos-policy "104" queue 2 queue-mgmt "QM_104_12500"
/configure qos vlan-qos-policy "104" queue 3 queue-mgmt "QM_104_12500"
/configure qos vlan-qos-policy "104" queue 5 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" queue 7 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" queue 8 percent-rate cir 100.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" description "IXR Network QoS"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 1 queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 2 queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 3 queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 3 percent-rate cir 80.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 4 queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 4 percent-rate cir 80.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 5 queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 5 percent-rate pir 10.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 5 percent-rate cir 10.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 6 queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 7 queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 7 percent-rate cir 10.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 8 queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 8 percent-rate cir 20.0
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q1" mbs 12500
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q2" mbs 12500
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q3" mbs 9380
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q4" mbs 9380
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q5" mbs 10
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q6" mbs 10
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q7" mbs 2500
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q8" mbs 2500
/configure qos queue-mgmt-policy "QM_104_12500" mbs 12500
/configure qos ingress-classification-policy "100" description "Standard QOS"
/configure qos ingress-classification-policy "100" default-action fc l2
/configure qos ingress-classification-policy "102" dot1p 1 fc l2
/configure qos ingress-classification-policy "102" dot1p 1 profile out
/configure qos ingress-classification-policy "102" dot1p 3 fc l1
/configure qos ingress-classification-policy "102" dot1p 3 profile out
/configure qos ingress-classification-policy "102" dot1p 4 fc h2
/configure qos ingress-classification-policy "102" dot1p 4 profile in
/configure qos ingress-classification-policy "102" dot1p 6 fc ef
/configure qos ingress-classification-policy "102" dot1p 6 profile in
/configure qos ingress-classification-policy "102" dscp be fc l2
/configure qos ingress-classification-policy "102" dscp be profile out
/configure qos ingress-classification-policy "102" dscp af11 fc l2
/configure qos ingress-classification-policy "102" dscp af11 profile out
/configure qos ingress-classification-policy "102" dscp af31 fc l1
/configure qos ingress-classification-policy "102" dscp af31 profile out
/configure qos ingress-classification-policy "102" dscp af41 fc h2
/configure qos ingress-classification-policy "102" dscp af41 profile in
/configure qos ingress-classification-policy "102" dscp ef fc ef
/configure qos ingress-classification-policy "102" dscp ef profile in
/configure qos ingress-classification-policy "103" dscp be fc l2
/configure qos ingress-classification-policy "103" dscp be profile out
/configure qos ingress-classification-policy "103" dscp af11 fc l2
/configure qos ingress-classification-policy "103" dscp af11 profile out
/configure qos ingress-classification-policy "103" dscp af21 fc l1
/configure qos ingress-classification-policy "103" dscp af21 profile out
/configure qos ingress-classification-policy "103" dscp af31 fc l1
/configure qos ingress-classification-policy "103" dscp af31 profile out
/configure qos ingress-classification-policy "103" dscp af32 fc l1
/configure qos ingress-classification-policy "103" dscp af32 profile in
/configure qos ingress-classification-policy "103" dscp af33 fc l1
/configure qos ingress-classification-policy "103" dscp af33 profile in
/configure qos ingress-classification-policy "103" dscp af41 fc h2
/configure qos ingress-classification-policy "103" dscp af41 profile in
/configure qos ingress-classification-policy "103" dscp ef fc ef
/configure qos ingress-classification-policy "103" dscp ef profile in
/configure qos ingress-classification-policy "103" dscp nc2 fc nc
/configure qos ingress-classification-policy "103" dscp nc2 profile in
/configure qos ingress-classification-policy "104" dot1p 0 fc l2
/configure qos ingress-classification-policy "104" dot1p 0 profile out
/configure qos ingress-classification-policy "104" dot1p 3 fc l1
/configure qos ingress-classification-policy "104" dot1p 3 profile out
/configure qos ingress-classification-policy "104" dot1p 4 fc h2
/configure qos ingress-classification-policy "104" dot1p 4 profile out
/configure qos ingress-classification-policy "104" dot1p 5 fc ef
/configure qos ingress-classification-policy "104" dot1p 5 profile out
/configure qos ingress-classification-policy "104" dot1p 6 fc h1
/configure qos ingress-classification-policy "104" dot1p 6 profile out
/configure qos ingress-classification-policy "104" dot1p 7 fc nc
/configure qos ingress-classification-policy "104" dot1p 7 profile out
/configure qos ingress-classification-policy "104" dscp be fc l2
/configure qos ingress-classification-policy "104" dscp be profile out
/configure qos ingress-classification-policy "104" dscp af11 fc l2
/configure qos ingress-classification-policy "104" dscp af11 profile out
/configure qos ingress-classification-policy "104" dscp af21 fc l2
/configure qos ingress-classification-policy "104" dscp af21 profile out
/configure qos ingress-classification-policy "104" dscp af22 fc l1
/configure qos ingress-classification-policy "104" dscp af22 profile out
/configure qos ingress-classification-policy "104" dscp af31 fc l1
/configure qos ingress-classification-policy "104" dscp af31 profile out
/configure qos ingress-classification-policy "104" dscp af41 fc l1
/configure qos ingress-classification-policy "104" dscp af41 profile out
/configure qos ingress-classification-policy "104" dscp af42 fc h2
/configure qos ingress-classification-policy "104" dscp af42 profile in
/configure qos ingress-classification-policy "104" dscp ef fc ef
/configure qos ingress-classification-policy "104" dscp ef profile in
/configure qos ingress-classification-policy "104" dscp nc2 fc h1
/configure qos ingress-classification-policy "104" dscp nc2 profile in
/configure qos ingress-classification-policy "110" description "Real Time VBR QOS"
/configure qos ingress-classification-policy "110" default-action fc h2
/configure qos ingress-classification-policy "110" default-action profile in
/configure qos ingress-classification-policy "120" description "Signalling QOS"
/configure qos ingress-classification-policy "120" default-action fc h1
/configure qos ingress-classification-policy "120" default-action profile in
/configure qos ingress-classification-policy "130" description "Critical Data OP QOS"
/configure qos ingress-classification-policy "130" default-action fc af
/configure qos ingress-classification-policy "140" description "Critical Data IP QOS"
/configure qos ingress-classification-policy "140" default-action fc l1
/configure qos ingress-classification-policy "140" default-action profile in
/configure qos ingress-classification-policy "150" description "Real Time CBR QOS"
/configure qos ingress-classification-policy "150" default-action fc ef
/configure qos ingress-classification-policy "150" default-action profile in
/configure qos ingress-classification-policy "160" description "Network Control QOS"
/configure qos ingress-classification-policy "160" default-action fc nc
/configure qos ingress-classification-policy "160" default-action profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" description "NQ_VFQ_IXR_INGRESS"
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" default-action fc l2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp be fc l2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp be profile out
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af11 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af11 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af12 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af12 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af13 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af13 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs2 fc h1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs2 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af21 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af21 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af22 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af22 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af23 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af23 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs3 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs3 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af31 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af31 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af32 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af32 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af33 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af33 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af41 fc h1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af41 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af42 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af42 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs5 fc h2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs5 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp ef fc ef
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp ef profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp nc1 fc nc
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp nc1 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 0 fc l2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 0 profile out
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 1 fc h2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 1 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 2 fc h1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 2 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 3 fc af
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 3 profile out
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 4 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 4 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 5 fc ef
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 5 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 6 fc nc
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 6 profile in
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" ingress-classification-policy "NQ_VFQ_IXR_Ing_class"
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 1 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 2 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 3 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 4 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 5 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 6 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 7 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 8 stat-mode offered-profile-with-discards
/configure qos egress-remark-policy "102" description "User Traffic delivered to full IP BTS"
/configure qos egress-remark-policy "102" fc ef dot1p in-profile 6
/configure qos egress-remark-policy "102" fc ef dot1p out-profile 6
/configure qos egress-remark-policy "103" fc l2 dot1p in-profile 0
/configure qos egress-remark-policy "103" fc l2 dot1p out-profile 0
/configure qos egress-remark-policy "103" fc h2 dot1p in-profile 5
/configure qos egress-remark-policy "103" fc h2 dot1p out-profile 5
/configure qos egress-remark-policy "103" fc ef dot1p in-profile 6
/configure qos egress-remark-policy "103" fc ef dot1p out-profile 6
/configure qos egress-remark-policy "103" fc nc dot1p in-profile 0
/configure qos egress-remark-policy "103" fc nc dot1p out-profile 0
/configure qos egress-remark-policy "104" fc l2 dot1p in-profile 0
/configure qos egress-remark-policy "104" fc l2 dot1p out-profile 0
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l2 lsp-exp in-profile 0
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l2 lsp-exp out-profile 0
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc af lsp-exp in-profile 3
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc af lsp-exp out-profile 3
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l1 lsp-exp in-profile 4
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l1 lsp-exp out-profile 3
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h2 lsp-exp in-profile 1
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h2 lsp-exp out-profile 1
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h1 lsp-exp in-profile 2
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h1 lsp-exp out-profile 2
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc nc lsp-exp in-profile 6
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc nc lsp-exp out-profile 6
/configure router "Base" autonomous-system 48728
/configure router "Base" ecmp 4
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" port {data["port-a1"]}
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" egress qos vlan-qos-policy policy-name "NQ_VFQ_IXR_VLAN_QOS"
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" egress qos egress-remark-policy policy-name "NQ_VFQ_IXR_Eg_Remark"
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" ingress qos network-ingress policy-name "NQ_VFQ_IXR_Net_Ing"
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" ipv4 primary address {data["network-a"]}
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" ipv4 primary prefix-length 31
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" port {data["port-b1"]}
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" egress qos vlan-qos-policy policy-name "NQ_VFQ_IXR_VLAN_QOS"
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" egress qos egress-remark-policy policy-name "NQ_VFQ_IXR_Eg_Remark"
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" ingress qos network-ingress policy-name "NQ_VFQ_IXR_Net_Ing"
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" ipv4 primary address {data["network-b"]}
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" ipv4 primary prefix-length 31
/configure router "Base" interface "lbl-bgp-lpbck" loopback
/configure router "Base" interface "lbl-bgp-lpbck" ipv4 primary address {data["loopback"]}
/configure router "Base" interface "lbl-bgp-lpbck" ipv4 primary prefix-length 32
/configure router "Base" interface "system" ipv4 primary address {data["system"]}
/configure router "Base" interface "system" ipv4 primary prefix-length 32
/configure router "Base" bgp min-route-advertisement 5
/configure router "Base" bgp rapid-withdrawal true
/configure router "Base" bgp peer-ip-tracking true
/configure router "Base" bgp ebgp-default-reject-policy import false
/configure router "Base" bgp ebgp-default-reject-policy export false
/configure router "Base" bgp next-hop-resolution labeled-routes transport-tunnel family vpn resolution-filter rsvp true
/configure router "Base" bgp next-hop-resolution labeled-routes transport-tunnel family label-ipv4 resolution-filter rsvp true
/configure router "Base" {{ bgp outbound-route-filtering extended-community send-orf }}
/configure router "Base" bgp group "POC2-lbgp-ipv4" peer-as 48728
/configure router "Base" bgp group "POC2-lbgp-ipv4" family ipv4 true
/configure router "Base" bgp group "POC2-lbgp-ipv4" import policy ["import-from-POC2"]
/configure router "Base" bgp group "POC2-lbgp-ipv4" export policy ["export-to-POC2"]
/configure router "Base" bgp group "Seamless_l3vpns_mp_ibgp" peer-as 48728
/configure router "Base" bgp group "Seamless_l3vpns_mp_ibgp" local-address 192.168.64.111
/configure router "Base" bgp group "Seamless_l3vpns_mp_ibgp" family vpn-ipv4 true
/configure router "Base" bgp neighbor {data["POC2-1"]} group "POC2-lbgp-ipv4"
/configure router "Base" bgp neighbor {data["POC2-1"]} authentication-key VFQatar
/configure router "Base" bgp neighbor {data["POC2-1"]} family label-ipv4 true
/configure router "Base" bgp neighbor {data["POC2-2"]} group "POC2-lbgp-ipv4"
/configure router "Base" bgp neighbor {data["POC2-2"]} authentication-key VFQatar
/configure router "Base" bgp neighbor {data["POC2-2"]} family label-ipv4 true
/configure router "Base" bgp neighbor {data["POC3-1"]} group "Seamless_l3vpns_mp_ibgp"
/configure router "Base" bgp neighbor {data["POC3-2"]} group "Seamless_l3vpns_mp_ibgp"
/configure router "Base" isis 0 admin-state enable
/configure router "Base" isis 0 authentication-key ALU
/configure router "Base" isis 0 authentication-type message-digest
/configure router "Base" isis 0 iid-tlv true
/configure router "Base" isis 0 lsp-lifetime 65535
/configure router "Base" isis 0 traffic-engineering true
/configure router "Base" isis 0 area-address [49.0974]
/configure router "Base" isis 0 timers spf-wait spf-max-wait 2000
/configure router "Base" isis 0 timers spf-wait spf-initial-wait 50
/configure router "Base" isis 0 timers spf-wait spf-second-wait 100
/configure router "Base" isis 0 timers lsp-wait lsp-max-wait 8000
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-key VFQatar
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-type message-digest
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" interface-type point-to-point
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" level-capability 1
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 hello-interval 10
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 metric 100
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-key VFQatar
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-type message-digest
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" interface-type point-to-point
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" level-capability 1
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 hello-interval 10
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 metric 100
/configure router "Base" {{ isis 0 interface "system" }}
/configure router "Base" isis 0 level 1 wide-metrics-only true
/configure router "Base" isis 0 level 2 wide-metrics-only true
/configure router "Base" isis {data["isis-a-area"]} admin-state enable
/configure router "Base" isis {data["isis-a-area"]} authentication-key ALU
/configure router "Base" isis {data["isis-a-area"]} authentication-type message-digest
/configure router "Base" isis {data["isis-a-area"]} all-l1isis 01:80:c2:00:01:00
/configure router "Base" isis {data["isis-a-area"]} all-l2isis 01:80:c2:00:01:11
/configure router "Base" isis {data["isis-a-area"]} iid-tlv true
/configure router "Base" isis {data["isis-a-area"]} lsp-lifetime 65535
/configure router "Base" isis {data["isis-a-area"]} traffic-engineering true
/configure router "Base" isis {data["isis-a-area"]} area-address [49.0974]
/configure router "Base" isis {data["isis-a-area"]} timers spf-wait spf-max-wait 2000
/configure router "Base" isis {data["isis-a-area"]} timers spf-wait spf-initial-wait 50
/configure router "Base" isis {data["isis-a-area"]} timers spf-wait spf-second-wait 100
/configure router "Base" isis {data["isis-a-area"]} timers lsp-wait lsp-max-wait 8000
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-key VFQatar
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-type message-digest
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" interface-type point-to-point
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" level-capability 1
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 hello-interval 10
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 metric 100
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-key VFQatar
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-type message-digest
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" interface-type point-to-point
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" level-capability 1
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 hello-interval 10
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 metric 100
/configure router "Base" {{ isis {data["isis-a-area"]} interface "system" }}
/configure router "Base" isis {data["isis-a-area"]} level 1 external-preference 163
/configure router "Base" isis {data["isis-a-area"]} level 1 preference 25
/configure router "Base" isis {data["isis-a-area"]} level 1 wide-metrics-only true
/configure router "Base" {{ ldp interface-parameters interface "NET_{data["far-end-a"]}_{data["network-a"]}" ipv4 }}
/configure router "Base" {{ ldp interface-parameters interface "NET_{data["far-end-b"]}_{data["network-b"]}" ipv4 }}
/configure router "Base" static-routes route 10.100.20.10/31 route-type unicast next-hop {increment_last_octet(data["network-a"])} admin-state enable
/configure router "Base" static-routes route 10.100.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-a"])} admin-state enable
/configure router "Base" static-routes route 10.200.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-a"])} admin-state enable
/configure router "Base" static-routes route 10.100.20.10/31 route-type unicast next-hop {increment_last_octet(data["network-b"])} admin-state enable
/configure router "Base" static-routes route 10.100.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-b"])} admin-state enable
/configure router "Base" static-routes route 10.200.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-b"])} admin-state enable
/configure service vprn "17804" admin-state enable
/configure service vprn "17804" description "eNB IPsec Public eUTRAN VPRN"
/configure service vprn "17804" customer "1"
/configure service vprn "17804" autonomous-system 48728
/configure service vprn "17804" bgp-ipvpn mpls admin-state enable
/configure service vprn "17804" bgp-ipvpn mpls route-distinguisher "48728:17804{data["Site"]}"
/configure service vprn "17804" bgp-ipvpn mpls vrf-target community "target:48728:178040"
/configure service vprn "17804" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17804" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17804" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "17812" admin-state enable
/configure service vprn "17812" description "BTS_BSC_Abis_VPRN"
/configure service vprn "17812" customer "1"
/configure service vprn "17812" autonomous-system 48728
/configure service vprn "17812" bgp-ipvpn mpls admin-state enable
/configure service vprn "17812" bgp-ipvpn mpls route-distinguisher "48728:17812{data["Site"]}"
/configure service vprn "17812" bgp-ipvpn mpls vrf-target community "target:48728:17812"
/configure service vprn "17812" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17812" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17812" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "17813" admin-state enable
/configure service vprn "17813" description "eNB_RNC_IuB_VPRN"
/configure service vprn "17813" customer "1"
/configure service vprn "17813" autonomous-system 48728
/configure service vprn "17813" bgp-ipvpn mpls admin-state enable
/configure service vprn "17813" bgp-ipvpn mpls route-distinguisher "48728:17813{data["Site"]}"
/configure service vprn "17813" bgp-ipvpn mpls vrf-target community "target:48728:17813"
/configure service vprn "17813" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17813" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17813" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "17815" admin-state enable
/configure service vprn "17815" description "Huawei OAM VPRN"
/configure service vprn "17815" customer "1"
/configure service vprn "17815" autonomous-system 48728
/configure service vprn "17815" bgp-ipvpn mpls admin-state enable
/configure service vprn "17815" bgp-ipvpn mpls route-distinguisher "48728:17815{data["Site"]}"
/configure service vprn "17815" bgp-ipvpn mpls vrf-target community "target:48728:17815"
/configure service vprn "17815" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17815" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17815" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "ENT-4G-5G_Public" description "ENT 4G-5G Public Service"
/configure service vprn "ENT-4G-5G_Public" service-id 55000
/configure service vprn "ENT-4G-5G_Public" customer "1"
/configure service vprn "ENT-4G-5G_Public" autonomous-system 48728
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls admin-state enable
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls route-distinguisher "48728:55000{data["Site"]}"
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls vrf-target community "target:65100:55000"
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure system name {data["hostname"]}
/configure system central-frequency-clock ql-selection true
/configure system central-frequency-clock revert true
/configure system central-frequency-clock ref1 admin-state enable
/configure system central-frequency-clock ref1 source-port {data["port-a1"]}
/configure management-interface configuration-mode mixed
/configure management-interface snmp packet-size 9216
/configure management-interface snmp streaming admin-state enable
/configure system security telnet-server true
/configure system security ftp-server true
/configure system security aaa local-profiles profile "ARCH2" default-action deny-all
/configure system security aaa local-profiles profile "ARCH2" entry 1 match "oam"
/configure system security aaa local-profiles profile "ARCH2" entry 1 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 2 match "ping"
/configure system security aaa local-profiles profile "ARCH2" entry 2 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 3 match "admin display-config"
/configure system security aaa local-profiles profile "ARCH2" entry 3 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 4 match "configure port"
/configure system security aaa local-profiles profile "ARCH2" entry 4 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 5 match "telnet"
/configure system security aaa local-profiles profile "ARCH2" entry 5 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 6 match "back"
/configure system security aaa local-profiles profile "ARCH2" entry 6 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 7 match "show"
/configure system security aaa local-profiles profile "ARCH2" entry 7 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 8 match "ssh"
/configure system security aaa local-profiles profile "ARCH2" entry 8 action deny
/configure system security aaa local-profiles profile "ARCH2" entry 9 match "traceroute"
/configure system security aaa local-profiles profile "ARCH2" entry 9 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 10 match "monitor"
/configure system security aaa local-profiles profile "ARCH2" entry 10 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 11 match "admin save"
/configure system security aaa local-profiles profile "ARCH2" entry 11 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 12 match "configure service vprn"
/configure system security aaa local-profiles profile "ARCH2" entry 12 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 13 match "environment more "
/configure system security aaa local-profiles profile "ARCH2" entry 13 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 14 match "info"
/configure system security aaa local-profiles profile "ARCH2" entry 14 action permit
/configure system security aaa local-profiles profile "Monitoring" default-action deny-all
/configure system security aaa local-profiles profile "Monitoring" entry 10 match "exec"
/configure system security aaa local-profiles profile "Monitoring" entry 10 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 20 match "help"
/configure system security aaa local-profiles profile "Monitoring" entry 20 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 30 match "logout"
/configure system security aaa local-profiles profile "Monitoring" entry 30 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 40 match "password"
/configure system security aaa local-profiles profile "Monitoring" entry 40 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 50 match "show"
/configure system security aaa local-profiles profile "Monitoring" entry 50 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 60 match "enable-admin"
/configure system security aaa local-profiles profile "Monitoring" entry 60 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 70 match "configure"
/configure system security aaa local-profiles profile "Monitoring" entry 70 action deny
/configure system security aaa local-profiles profile "Monitoring" entry 80 match "admin display-config"
/configure system security aaa local-profiles profile "Monitoring" entry 80 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 90 match "show config"
/configure system security aaa local-profiles profile "Monitoring" entry 90 action deny
/configure system security aaa local-profiles profile "Monitoring" entry 110 match "traceroute"
/configure system security aaa local-profiles profile "Monitoring" entry 110 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 120 match "exit"
/configure system security aaa local-profiles profile "Monitoring" entry 120 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 130 match "configure li"
/configure system security aaa local-profiles profile "Monitoring" entry 130 action deny
/configure system security aaa local-profiles profile "Monitoring" entry 140 match "ping"
/configure system security aaa local-profiles profile "Monitoring" entry 140 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 150 match "telnet"
/configure system security aaa local-profiles profile "Monitoring" entry 150 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 160 match "monitor port"
/configure system security aaa local-profiles profile "Monitoring" entry 160 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 170 match "monitor lag"
/configure system security aaa local-profiles profile "Monitoring" entry 170 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 180 match "admin save"
/configure system security aaa local-profiles profile "Monitoring" entry 180 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 190 match "admin tech-support"
/configure system security aaa local-profiles profile "Monitoring" entry 190 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 200 match "history"
/configure system security aaa local-profiles profile "Monitoring" entry 200 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 210 match "file"
/configure system security aaa local-profiles profile "Monitoring" entry 210 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 211 match "ssh"
/configure system security aaa local-profiles profile "Monitoring" entry 211 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 212 match "oam lsp-trace"
/configure system security aaa local-profiles profile "Monitoring" entry 212 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 213 match "clear port"
/configure system security aaa local-profiles profile "Monitoring" entry 213 action permit
/configure system security aaa local-profiles profile "NokiaProject" default-action permit-all
/configure system security aaa local-profiles profile "NokiaProject" entry 1 description "reboot"
/configure system security aaa local-profiles profile "NokiaProject" entry 1 match "admin reboot"
/configure system security aaa local-profiles profile "NokiaProject" entry 1 action deny
/configure system security aaa local-profiles profile "NokiaProject" entry 2 description "securty"
/configure system security aaa local-profiles profile "NokiaProject" entry 2 match "configure system security"
/configure system security aaa local-profiles profile "NokiaProject" entry 2 action deny
/configure system security aaa local-profiles profile "Operator" default-action permit-all
/configure system security aaa local-profiles profile "Operator" entry 10 match "configure system security"
/configure system security aaa local-profiles profile "Operator" entry 10 action deny
/configure system security aaa local-profiles profile "Operator" entry 20 match "configure li"
/configure system security aaa local-profiles profile "Operator" entry 20 action deny
/configure system security aaa local-profiles profile "Operator" entry 30 match "show li"
/configure system security aaa local-profiles profile "Operator" entry 30 action deny
/configure system security aaa local-profiles profile "Operator" entry 50 match "configure filter"
/configure system security aaa local-profiles profile "Operator" entry 50 action deny
/configure system security aaa local-profiles profile "SOC" default-action deny-all
/configure system security aaa local-profiles profile "SOC" entry 8 match "configure router interface"
/configure system security aaa local-profiles profile "SOC" entry 8 action permit
/configure system security aaa local-profiles profile "SOC" entry 9 description "Router reboot"
/configure system security aaa local-profiles profile "SOC" entry 9 match "admin reboot"
/configure system security aaa local-profiles profile "SOC" entry 9 action deny
/configure system security aaa local-profiles profile "SOC" entry 20 match "configure router bgp"
/configure system security aaa local-profiles profile "SOC" entry 20 action permit
/configure system security aaa local-profiles profile "SOC" entry 70 match "admin display-config"
/configure system security aaa local-profiles profile "SOC" entry 70 action permit
/configure system security aaa local-profiles profile "SOC" entry 80 match "show"
/configure system security aaa local-profiles profile "SOC" entry 80 action permit
/configure system security aaa local-profiles profile "SOC" entry 90 match "monitor"
/configure system security aaa local-profiles profile "SOC" entry 90 action permit
/configure system security aaa local-profiles profile "SOC" entry 100 match "telnet"
/configure system security aaa local-profiles profile "SOC" entry 100 action permit
/configure system security aaa local-profiles profile "SOC" entry 110 match "ssh"
/configure system security aaa local-profiles profile "SOC" entry 110 action permit
/configure system security aaa local-profiles profile "SOC" entry 120 match "oam"
/configure system security aaa local-profiles profile "SOC" entry 120 action permit
/configure system security aaa local-profiles profile "SOC" entry 140 match "configure router policy-options"
/configure system security aaa local-profiles profile "SOC" entry 140 action permit
/configure system security aaa local-profiles profile "SOC" entry 150 match "configure port"
/configure system security aaa local-profiles profile "SOC" entry 150 action permit
/configure system security aaa local-profiles profile "SOC" entry 160 match "info"
/configure system security aaa local-profiles profile "SOC" entry 160 action permit
/configure system security aaa local-profiles profile "SOC" entry 170 match "ping"
/configure system security aaa local-profiles profile "SOC" entry 170 action permit
/configure system security aaa local-profiles profile "SOC" entry 180 match "traceroute"
/configure system security aaa local-profiles profile "SOC" entry 180 action permit
/configure system security aaa local-profiles profile "SOC" entry 190 match "admin tech-support"
/configure system security aaa local-profiles profile "SOC" entry 190 action permit
/configure system security aaa local-profiles profile "SOC" entry 200 match "history"
/configure system security aaa local-profiles profile "SOC" entry 200 action permit
/configure system security aaa local-profiles profile "SOC" entry 210 match "configure service"
/configure system security aaa local-profiles profile "SOC" entry 210 action permit
/configure system security aaa local-profiles profile "SOC" entry 220 match "exit"
/configure system security aaa local-profiles profile "SOC" entry 220 action permit
/configure system security aaa local-profiles profile "SOC" entry 230 match "admin save"
/configure system security aaa local-profiles profile "SOC" entry 230 action permit
/configure system security aaa local-profiles profile "SOC" entry 240 match "pwc"
/configure system security aaa local-profiles profile "SOC" entry 240 action permit
/configure system security aaa local-profiles profile "SOC" entry 250 match "back"
/configure system security aaa local-profiles profile "SOC" entry 250 action permit
/configure system security aaa local-profiles profile "SOC" entry 260 match "clear"
/configure system security aaa local-profiles profile "SOC" entry 260 action permit
/configure system security aaa local-profiles profile "SOC" entry 270 match "configure lag"
/configure system security aaa local-profiles profile "SOC" entry 270 action permit
/configure system security aaa local-profiles profile "SOC" entry 280 match "configure qos"
/configure system security aaa local-profiles profile "SOC" entry 280 action permit
/configure system security aaa local-profiles profile "SOC" entry 290 match "environment"
/configure system security aaa local-profiles profile "SOC" entry 290 action deny
/configure system security aaa local-profiles profile "TPM" entry 10 match "exec"
/configure system security aaa local-profiles profile "TPM" entry 10 action permit
/configure system security aaa local-profiles profile "TPM" entry 20 match "exit"
/configure system security aaa local-profiles profile "TPM" entry 20 action permit
/configure system security aaa local-profiles profile "TPM" entry 30 match "help"
/configure system security aaa local-profiles profile "TPM" entry 30 action permit
/configure system security aaa local-profiles profile "TPM" entry 40 match "logout"
/configure system security aaa local-profiles profile "TPM" entry 40 action permit
/configure system security aaa local-profiles profile "TPM" entry 41 match "tools dump"
/configure system security aaa local-profiles profile "TPM" entry 41 action permit
/configure system security aaa local-profiles profile "TPM" entry 42 match "sleep"
/configure system security aaa local-profiles profile "TPM" entry 42 action permit
/configure system security aaa local-profiles profile "TPM" entry 43 match "file dir"
/configure system security aaa local-profiles profile "TPM" entry 43 action permit
/configure system security aaa local-profiles profile "TPM" entry 44 match "environment more"
/configure system security aaa local-profiles profile "TPM" entry 44 action permit
/configure system security aaa local-profiles profile "TPM" entry 50 match "password"
/configure system security aaa local-profiles profile "TPM" entry 50 action permit
/configure system security aaa local-profiles profile "TPM" entry 53 match "admin display-config"
/configure system security aaa local-profiles profile "TPM" entry 53 action permit
/configure system security aaa local-profiles profile "TPM" entry 55 match "configure"
/configure system security aaa local-profiles profile "TPM" entry 55 action deny
/configure system security aaa local-profiles profile "TPM" entry 60 match "show config"
/configure system security aaa local-profiles profile "TPM" entry 60 action deny
/configure system security aaa local-profiles profile "TPM" entry 65 match "show li"
/configure system security aaa local-profiles profile "TPM" entry 65 action deny
/configure system security aaa local-profiles profile "TPM" entry 70 match "show"
/configure system security aaa local-profiles profile "TPM" entry 70 action permit
/configure system security aaa local-profiles profile "TPM" entry 80 match "enable-admin"
/configure system security aaa local-profiles profile "TPM" entry 80 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 6 match "monitor"
/configure system security aaa local-profiles profile "VF-NSU" entry 6 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 10 match "exec"
/configure system security aaa local-profiles profile "VF-NSU" entry 10 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 30 match "help"
/configure system security aaa local-profiles profile "VF-NSU" entry 30 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 40 match "logout"
/configure system security aaa local-profiles profile "VF-NSU" entry 40 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 50 match "password"
/configure system security aaa local-profiles profile "VF-NSU" entry 50 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 60 match "admin display-config"
/configure system security aaa local-profiles profile "VF-NSU" entry 60 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 65 match "admin"
/configure system security aaa local-profiles profile "VF-NSU" entry 65 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 70 match "show"
/configure system security aaa local-profiles profile "VF-NSU" entry 70 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 80 match "enable-admin"
/configure system security aaa local-profiles profile "VF-NSU" entry 80 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 100 match "configure"
/configure system security aaa local-profiles profile "VF-NSU" entry 100 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 110 match "tools"
/configure system security aaa local-profiles profile "VF-NSU" entry 110 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 120 match "ping"
/configure system security aaa local-profiles profile "VF-NSU" entry 120 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 130 match "telnet"
/configure system security aaa local-profiles profile "VF-NSU" entry 130 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 140 match "traceroute"
/configure system security aaa local-profiles profile "VF-NSU" entry 140 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 150 match "exit"
/configure system security aaa local-profiles profile "VF-NSU" entry 150 action permit
/configure system security {{ aaa local-profiles profile "password" }}
/configure system security aaa local-profiles profile "show" default-action deny-all
/configure system security aaa local-profiles profile "show" entry 1 match "show"
/configure system security aaa local-profiles profile "show" entry 1 action permit
/configure system security aaa local-profiles profile "show" entry 2 match "admin display-config"
/configure system security aaa local-profiles profile "show" entry 2 action permit
/configure system security aaa local-profiles profile "show" entry 7 match "monitor"
/configure system security aaa local-profiles profile "show" entry 7 action permit
/configure system security aaa local-profiles profile "show" entry 8 match "ping"
/configure system security aaa local-profiles profile "show" entry 8 action permit
/configure system security aaa local-profiles profile "show" entry 9 match "telnet"
/configure system security aaa local-profiles profile "show" entry 9 action permit
/configure system security aaa local-profiles profile "tier-1" default-action deny-all
/configure system security aaa local-profiles profile "tier-1" entry 10 match "admin tech-support"
/configure system security aaa local-profiles profile "tier-1" entry 10 action permit
/configure system security aaa local-profiles profile "tier-1" entry 20 match "show"
/configure system security aaa local-profiles profile "tier-1" entry 20 action permit
/configure system security aaa local-profiles profile "tier-1" entry 30 match "exit"
/configure system security aaa local-profiles profile "tier-1" entry 30 action permit
/configure system security snmp access "nmsPriv" context "" security-model usm security-level privacy read "iso"
/configure system security snmp access "nmsPriv" context "" security-model usm security-level privacy write "iso"
/configure system security snmp access "nmsPriv" context "" security-model usm security-level privacy notify "iso"
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy prefix-match prefix
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy read "vprn-view"
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy write "vprn-view"
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy notify "iso"
/configure system security snmp community "76HzdddhlPpRo1Vql+ZB5spLqccgYQ== hash2" access-permissions r
/configure system security snmp community "76HzdddhlPpRo1Vql+ZB5spLqccgYQ== hash2" version v2c
/configure system security user-params local-user password complexity-rules required lowercase 1
/configure system security user-params local-user password complexity-rules required uppercase 1
/configure system security user-params local-user password complexity-rules required numeric 1
/configure system security user-params local-user password complexity-rules required special-character 1
/configure system security user-params local-user user "AdminSAM5620" password "$2y$10$QGGVBkdQhc.V9ceWwfl6..ynxeadOnjPSgFRiAXwGQa3pLGZsN7PK"
/configure system security user-params local-user user "AdminSAM5620" access console true
/configure system security user-params local-user user "AdminSAM5620" access ftp true
/configure system security user-params local-user user "AdminSAM5620" access snmp true
/configure system security user-params local-user user "AdminSAM5620" console member ["default" "administrative"]
/configure system security {{ user-params local-user user "AdminSAM5620" snmp authentication }}
/configure system security user-params local-user user "VFQ.arajeeb" password "$2y$10$.ITViSWCVNkgClQNo9TMY.3zg.gBQZCLjjNRY1WhIy.GkN8eC/6dy"
/configure system security user-params local-user user "VFQ.arajeeb" access console true
/configure system security user-params local-user user "VFQ.arajeeb" access ftp true
/configure system security user-params local-user user "VFQ.arajeeb" console member ["default" "Operator"]
/configure system security user-params local-user user "admin" password "$2y$10$lnMYTNLh3YK1G5e6bCzlg.hcCfnMQdu9HShe6CNxbUW3Li6Eazq4K"
/configure system security user-params local-user user "admin" access console true
/configure system security user-params local-user user "admin" access ftp true
/configure system security user-params local-user user "admin" access netconf true
/configure system security user-params local-user user "admin" access grpc true
/configure system security user-params local-user user "admin" console member ["administrative"]
/configure system security user-params local-user user "admin" public-keys ecdsa ecdsa-key 32 key-value "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIr3f6WDgc4OPwnTzCWQuzbDjMbhg+9Vnnlu5Wp2Wc5TLF4xQslbJVAxR38EYkJ5GZWoyvBktxa0NuQ5MxCZBqs="
/configure system security user-params local-user user "ameers" password "$2y$10$NMjfPL4Kauf1seZOSPcKc./9vc3JrMdoSF0HJlh8GS.kAmTCJHeVO"
/configure system security user-params local-user user "ameers" access console true
/configure system security user-params local-user user "ameers" access ftp true
/configure system security user-params local-user user "ameers" access snmp true
/configure system security user-params local-user user "ameers" console member ["default" "NokiaProject"]
/configure system security user-params local-user user "amogh.acharya" password "$2y$10$l2fFGhaiiVE8f0E5mYe62.L5RYheC6Xn1r6UcmiiOMqw5MskjRjqa"
/configure system security user-params local-user user "amogh.acharya" access console true
/configure system security user-params local-user user "amogh.acharya" console member ["default" "Operator"]
/configure system security user-params local-user user "anas.hammami" password "$2y$10$4UStCMbBpydY2jsaEcj9o./b49aloC0qZo7kgdgOXnRXz2jDFsKeW"
/configure system security user-params local-user user "anas.hammami" access console true
/configure system security user-params local-user user "anas.hammami" access ftp true
/configure system security user-params local-user user "anas.hammami" console member ["administrative"]
/configure system security user-params local-user user "chrisnanda.ent" password "$2y$10$/YtllkeV45TIzAFlkw0Ks.ZOxXjkhrbELh.ZSgivB0oan4lQMheje"
/configure system security user-params local-user user "chrisnanda.ent" access console true
/configure system security user-params local-user user "chrisnanda.ent" access ftp true
/configure system security user-params local-user user "chrisnanda.ent" console member ["default" "administrative"]
/configure system security user-params local-user user "deni.sartika" password "$2y$10$GPYPa.WMxyxF7TW79K09g.Y0FrP.C7HtIAPVGl8EltTGdPKDn/pi."
/configure system security user-params local-user user "deni.sartika" access console true
/configure system security user-params local-user user "deni.sartika" access ftp true
/configure system security user-params local-user user "deni.sartika" console member ["administrative"]
/configure system security user-params local-user user "gems.bo" password "$2y$10$tc0o3pEKR3en89sgtk2b2.KC9rwkw5L6pKvfF95n6787vowCmwUzm"
/configure system security user-params local-user user "gems.bo" access console true
/configure system security user-params local-user user "gems.bo" access ftp true
/configure system security user-params local-user user "gems.bo" console member ["default" "Operator"]
/configure system security user-params local-user user "gnocipfo" password "$2y$10$R7ZyDzV9J57tOW/Z3AX9..y0t/PdvBNWEo26.VcWDy77haJOjJHi6"
/configure system security user-params local-user user "gnocipfo" access console true
/configure system security user-params local-user user "gnocipfo" access ftp true
/configure system security user-params local-user user "gnocipfo" access snmp true
/configure system security user-params local-user user "gnocipfo" console member ["default" "show"]
/configure system security {{ user-params local-user user "gnocipfo" snmp authentication }}
/configure system security user-params local-user user "muhammad.ehsan" password "$2y$10$Sja5NHyihHEh1hvbMhHdo.ftFhjP1l7cXXMtVOB.dmlyP4EHcRscC"
/configure system security user-params local-user user "muhammad.ehsan" access console true
/configure system security user-params local-user user "muhammad.ehsan" access ftp true
/configure system security user-params local-user user "muhammad.ehsan" console member ["default" "Operator" "administrative"]
/configure system security user-params local-user user "rohitb" password "$2y$10$eyQrBfoT8Gi4XEd1EJexM.EHxOeBBzMlfBf/gVNZ3Ui2DqlocvXjS"
/configure system security user-params local-user user "rohitb" access console true
/configure system security user-params local-user user "rohitb" access ftp true
/configure system security user-params local-user user "rohitb" console member ["default" "administrative"]
/configure system security user-params local-user user "samcli" password "$2y$10$N5URo5oH0xQ7HBdxK1ms2.kgWEGE5xp0c96vhCEQ.bltHKykRIJe6"
/configure system security user-params local-user user "samcli" access console true
/configure system security user-params local-user user "samcli" console member ["administrative"]
/configure system security user-params local-user user "snmpv3user" password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
/configure system security user-params local-user user "snmpv3user" access snmp true
/configure system security user-params local-user user "snmpv3user" console member ["default"]
/configure system security user-params local-user user "snmpv3user" snmp group "nmsPriv"
/configure system security user-params local-user user "snmpv3user" snmp authentication authentication-protocol hmac-sha1-96
/configure system security user-params local-user user "snmpv3user" snmp authentication authentication-key "vzCgV2ozcprrQwCl/rp+bOe2SGtnkRuD4c0t0y6A7bY7LLkA hash2"
/configure system security user-params local-user user "snmpv3user" snmp authentication privacy privacy-protocol cbc-des
/configure system security user-params local-user user "snmpv3user" snmp authentication privacy privacy-key "supXCSZYiL+Ugo6/Jjb4tm5crAKmHOw35sP+EbMiAFc= hash2"
/configure system security user-params local-user user "vfq.mali" password "$2y$10$zhkSzfGw6ET8iTy7ZDxeA.4vlfqyNbfnl942oWLydTWFGHJ6t2enu"
/configure system security user-params local-user user "vfq.mali" access console true
/configure system security user-params local-user user "vfq.mali" access ftp true
/configure system security user-params local-user user "vfq.mali" console member ["default" "administrative"]
/configure system time ntp server 10.100.20.68 router-instance "Base" prefer true
/configure system time {{ ntp server 10.200.20.68 router-instance "Base" }}
/configure system time {{ ntp server 172.16.240.41 router-instance "Base" }}
/edit-config bof private
/bof configuration primary-location "cf3" / {data["hostname"]}.cfg"
/bof system persistent-indices true
commit
quit-config
"""
    return (txt)


def make_route_base_IXR_small_md(data):
    txt = f"""
/configure card 1 mda 1 sync-e true
/configure card 1 mda 1 mda-type m24-sfp++8-sfp28+2-qsfp28
/configure log accounting-policy 27 admin-state enable
/configure log accounting-policy 27 description "MBH drop statistic collection"
/configure log accounting-policy 27 collection-interval 15
/configure log accounting-policy 27 record service-egress-packets
/configure log accounting-policy 27 destination file "27"
/configure log accounting-policy 28 admin-state enable
/configure log accounting-policy 28 description "MBH Drop collection"
/configure log accounting-policy 28 collection-interval 15
/configure log accounting-policy 28 record service-ingress-packets
/configure log accounting-policy 28 destination file "38"
/configure log log-events system event smScriptResult generate true
/configure log log-events system event smScriptException generate true
/configure log log-events vrtr event tmnxVRtrStaticRouteStatusChanged generate true
/configure log file "9" rollover 2880
/configure log file "9" retention 500
/configure log file "9" compact-flash-location primary cf3
/configure log file "27" description "SAP drop collection"
/configure log file "27" rollover 15
/configure log file "27" retention 4
/configure log file "27" compact-flash-location primary cf3
/configure log file "38" description "MBH"
/configure log file "38" rollover 15
/configure log file "38" retention 4
/configure log file "38" compact-flash-location primary cf3
/configure log file "95" description "Main Log File"
/configure log file "95" rollover 360
/configure log file "95" retention 72
/configure log file "95" compact-flash-location primary cf3
/configure log filter "1001" named-entry "10" description "Collect only events of major severity or higher"
/configure log filter "1001" named-entry "10" action forward
/configure log filter "1001" named-entry "10" match severity gte major
/configure log log-id "9" time-format local
/configure log log-id "9" source change true
/configure log log-id "9" destination file "9"
/configure log log-id "14" source debug true
/configure log {{ log - id "14" destination memory }}
/configure log log-id "20" source debug true
/configure log log-id "95" source main true
/configure log log-id "95" destination file "95"
/configure log log-id "98" source main true
/configure log log-id "98" source security true
/configure log log-id "98" source change true
/configure log log-id "98" destination snmp max-entries 1024
/configure log log-id "99" description "Default System Log"
/configure log log-id "99" source main true
/configure log log-id "99" destination memory max-entries 500
/configure log log-id "100" description "Default Serious Errors Log"
/configure log log-id "100" filter "1001"
/configure log log-id "100" source main true
/configure log log-id "100" destination memory max-entries 500
/configure log snmp-trap-group "98" description "5620sam"
/configure log snmp-trap-group "98" trap-target "10.100.16.132:162" address 10.100.16.132
/configure log snmp-trap-group "98" trap-target "10.100.16.132:162" version snmpv2c
/configure log snmp-trap-group "98" trap-target "10.100.16.132:162" notify-community "citrix"
/configure log snmp-trap-group "98" trap-target "10.100.20.68:162" address 10.100.20.68
/configure log snmp-trap-group "98" trap-target "10.100.20.68:162" version snmpv2c
/configure log snmp-trap-group "98" trap-target "10.100.20.68:162" notify-community "privatetrap98"
/configure log snmp-trap-group "98" trap-target "10.200.20.68:162" address 10.200.20.68
/configure log snmp-trap-group "98" trap-target "10.200.20.68:162" version snmpv2c
/configure log snmp-trap-group "98" trap-target "10.200.20.68:162" notify-community "privatetrap98"
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main1" address 10.200.20.68
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main1" notify-community "snmpv3user"
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main1" security-level privacy
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main2" address 10.100.20.68
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main2" notify-community "snmpv3user"
/configure log snmp-trap-group "98" trap-target "D89D672883B8:main2" security-level privacy
/configure policy-options {{ community "service-lpbcks-IS0" member "48728:1110" }}
/configure policy-options {{ community "service-lpbcks-IS1" member "48728:1111" }}
/configure policy-options {{ community "service-lpbcks-IS2" member "48728:1112" }}
/configure policy-options {{ community "service-lpbcks-IS3" member "48728:1113" }}
/configure policy-options {{ community "service-lpbcks-IS4" member "48728:1114" }}
/configure policy-options {{ community "service-lpbcks-IS5" member "48728:1115" }}
/configure policy-options {{ community "service-lpbcks-IS6" member "48728:1116" }}
/configure policy-options {{ community "service-lpbcks-IS7" member "48728:1117" }}
/configure policy-options {{ community "service-lpbcks-IS8" member "48728:1118" }}
/configure policy-options {{ community "service-lpbcks-POC1" member "48728:11110" }}
/configure policy-options {{ prefix - list "lbl-bgp-lpbck" prefix {data["loopback"]} / 32 type exact }}
/configure policy-options prefix-list "only-lbl-bgp-lpbcks" prefix 192.168.64.0/20 type range start-length 32
/configure policy-options prefix-list "only-lbl-bgp-lpbcks" prefix 192.168.64.0/20 type range end-length 32
/configure policy-options policy-statement "export-to-POC2" entry 10 from prefix-list ["lbl-bgp-lpbck"]
/configure policy-options policy-statement "export-to-POC2" entry 10 action action-type accept
/configure policy-options policy-statement "export-to-POC2" entry 10 action origin igp
/configure policy-options policy-statement "export-to-POC2" entry 10 action community add ["service-lpbcks-IS1"]
/configure policy-options policy-statement "export-to-POC2" default-action action-type reject
/configure policy-options policy-statement "import-from-POC2" entry 10 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 10 from community name "service-lpbcks-IS{data["isis-a-area"]}"
/configure policy-options policy-statement "import-from-POC2" entry 10 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 10 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 20 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 20 from community name "service-lpbcks-POC1"
/configure policy-options policy-statement "import-from-POC2" entry 20 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 20 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 30 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 30 from community name "service-lpbcks-IS2"
/configure policy-options policy-statement "import-from-POC2" entry 30 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 30 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 40 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 40 from community name "service-lpbcks-IS3"
/configure policy-options policy-statement "import-from-POC2" entry 40 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 40 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 50 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 50 from community name "service-lpbcks-IS4"
/configure policy-options policy-statement "import-from-POC2" entry 50 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 50 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 60 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 60 from community name "service-lpbcks-IS5"
/configure policy-options policy-statement "import-from-POC2" entry 60 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 60 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 70 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 70 from community name "service-lpbcks-IS6"
/configure policy-options policy-statement "import-from-POC2" entry 70 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 70 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 80 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 80 from community name "service-lpbcks-IS7"
/configure policy-options policy-statement "import-from-POC2" entry 80 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 80 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 90 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 90 from community name "service-lpbcks-IS8"
/configure policy-options policy-statement "import-from-POC2" entry 90 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 90 action action-type accept
/configure policy-options policy-statement "import-from-POC2" entry 100 from prefix-list ["only-lbl-bgp-lpbcks"]
/configure policy-options policy-statement "import-from-POC2" entry 100 from community name "service-lpbcks-IS0"
/configure policy-options policy-statement "import-from-POC2" entry 100 from protocol name [bgp-label]
/configure policy-options policy-statement "import-from-POC2" entry 100 action action-type accept
/configure policy-options policy-statement "import-from-POC2" default-action action-type reject
/configure port {data["port-a1"]} admin-state enable
/configure port {data["port-a1"]} description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
/configure port {data["port-a1"]} ethernet collect-stats true
/configure port {data["port-a1"]} ethernet mtu 2102
/configure port {data["port-a1"]} ethernet ssm admin-state enable
/configure port {data["port-a1"]} ethernet egress port-qos-policy policy-name "NQ_VFQ_IXR_PORT_QOS"
/configure port {data["port-a1"]} ethernet network collect-stats true
/configure port {data["port-b1"]} admin-state enable
/configure port {data["port-b1"]} description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
/configure port {data["port-b1"]} ethernet collect-stats true
/configure port {data["port-b1"]} ethernet mtu 2102
/configure port {data["port-b1"]} ethernet ssm admin-state enable
/configure port {data["port-b1"]} ethernet egress port-qos-policy policy-name "NQ_VFQ_IXR_PORT_QOS"
/configure port {data["port-b1"]} ethernet network collect-stats true
/configure qos sap-ingress "102" description "Ingress for 2G full IP"
/configure qos sap-ingress "102" ingress-classification-policy "102"
/configure qos sap-ingress "102" policer 3 rate cir 100
/configure qos sap-ingress "102" policer 4 rate cir 100
/configure qos sap-ingress "102" policer 5 rate cir max
/configure qos sap-ingress "102" policer 6 rate cir max
/configure qos sap-ingress "102" policer 8 rate cir max
/configure qos sap-ingress "103" ingress-classification-policy "103"
/configure qos sap-ingress "103" policer 3 rate cir 100
/configure qos sap-ingress "103" policer 4 rate cir 100
/configure qos sap-ingress "103" policer 5 rate cir max
/configure qos sap-ingress "103" policer 6 rate cir max
/configure qos sap-ingress "103" policer 8 rate cir max
/configure qos sap-ingress "104" description "4G LTE SAP Ingress policy"
/configure qos sap-ingress "104" ingress-classification-policy "104"
/configure qos sap-ingress "104" policer 1 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 1 mbs 12800000
/configure qos sap-ingress "104" policer 1 cbs 6400000
/configure qos sap-ingress "104" policer 2 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 2 mbs 12800000
/configure qos sap-ingress "104" policer 2 cbs 6400000
/configure qos sap-ingress "104" policer 3 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 4 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 5 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 5 rate cir max
/configure qos sap-ingress "104" policer 6 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 6 rate cir max
/configure qos sap-ingress "104" policer 7 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 7 rate cir max
/configure qos sap-ingress "104" policer 8 stat-mode offered-profile-with-discards
/configure qos sap-ingress "104" policer 8 rate cir max
/configure qos sap-ingress "110" description "Real Time VBR QOS"
/configure qos sap-ingress "110" ingress-classification-policy "110"
/configure qos sap-ingress "120" description "Signalling QOS"
/configure qos sap-ingress "120" ingress-classification-policy "120"
/configure qos sap-ingress "120" policer 7 rate cir max
/configure qos sap-ingress "130" description "Critical Data OP QOS"
/configure qos sap-ingress "130" ingress-classification-policy "130"
/configure qos sap-ingress "140" description "Critical Data IP QOS"
/configure qos sap-ingress "140" ingress-classification-policy "140"
/configure qos sap-ingress "150" description "Real Time CBR QOS"
/configure qos sap-ingress "150" ingress-classification-policy "150"
/configure qos sap-ingress "150" policer 6 rate cir max
/configure qos sap-ingress "160" description "Network Control QOS"
/configure qos sap-ingress "160" ingress-classification-policy "160"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" description "IXR Network QoS"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 1 queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 2 queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 3 queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 3 scheduler-mode wfq percent-rate cir 80.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 4 queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 4 scheduler-mode wfq percent-rate cir 80.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 5 queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 5 scheduler-mode wfq percent-rate pir 10.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 5 scheduler-mode wfq percent-rate cir 10.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 6 queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 6 scheduler-mode wfq percent-rate cir 100.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 7 queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 7 scheduler-mode wfq percent-rate cir 10.0
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 8 queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
/configure qos port-qos-policy "NQ_VFQ_IXR_PORT_QOS" queue 8 scheduler-mode wfq percent-rate cir 20.0
/configure qos vlan-qos-policy "102" description "Egress for 2G full IP"
/configure qos vlan-qos-policy "102" queue 5 percent-rate cir 100.0
/configure qos vlan-qos-policy "102" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "102" queue 8 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" description "User Traffic delivered to full IP nodeB"
/configure qos vlan-qos-policy "103" queue 3 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 4 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 5 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 6 queue-forwarding-type expedite-hi
/configure qos vlan-qos-policy "103" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "103" queue 8 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" description "4G LTE SAP Egress policy"
/configure qos vlan-qos-policy "104" queue 1 queue-mgmt "QM_104_12500"
/configure qos vlan-qos-policy "104" queue 2 queue-mgmt "QM_104_12500"
/configure qos vlan-qos-policy "104" queue 3 queue-mgmt "QM_104_12500"
/configure qos vlan-qos-policy "104" queue 5 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" queue 7 percent-rate cir 100.0
/configure qos vlan-qos-policy "104" queue 8 percent-rate cir 100.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" description "IXR Network QoS"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 1 queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 2 queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 3 queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 3 percent-rate cir 80.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 4 queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 4 percent-rate cir 80.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 5 queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 5 percent-rate pir 10.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 5 percent-rate cir 10.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 6 queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 6 percent-rate cir 100.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 7 queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 7 percent-rate cir 10.0
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 8 queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
/configure qos vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" queue 8 percent-rate cir 20.0
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q1" mbs 12500
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q2" mbs 12500
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q3" mbs 9380
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q4" mbs 9380
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q5" mbs 10
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q6" mbs 10
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q7" mbs 2500
/configure qos queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q8" mbs 2500
/configure qos queue-mgmt-policy "QM_104_12500" mbs 12500
/configure qos ingress-classification-policy "100" description "Standard QOS"
/configure qos ingress-classification-policy "100" default-action fc l2
/configure qos ingress-classification-policy "102" dot1p 1 fc l2
/configure qos ingress-classification-policy "102" dot1p 1 profile out
/configure qos ingress-classification-policy "102" dot1p 3 fc l1
/configure qos ingress-classification-policy "102" dot1p 3 profile out
/configure qos ingress-classification-policy "102" dot1p 4 fc h2
/configure qos ingress-classification-policy "102" dot1p 4 profile in
/configure qos ingress-classification-policy "102" dot1p 6 fc ef
/configure qos ingress-classification-policy "102" dot1p 6 profile in
/configure qos ingress-classification-policy "102" dscp be fc l2
/configure qos ingress-classification-policy "102" dscp be profile out
/configure qos ingress-classification-policy "102" dscp af11 fc l2
/configure qos ingress-classification-policy "102" dscp af11 profile out
/configure qos ingress-classification-policy "102" dscp af31 fc l1
/configure qos ingress-classification-policy "102" dscp af31 profile out
/configure qos ingress-classification-policy "102" dscp af41 fc h2
/configure qos ingress-classification-policy "102" dscp af41 profile in
/configure qos ingress-classification-policy "102" dscp ef fc ef
/configure qos ingress-classification-policy "102" dscp ef profile in
/configure qos ingress-classification-policy "103" dscp be fc l2
/configure qos ingress-classification-policy "103" dscp be profile out
/configure qos ingress-classification-policy "103" dscp af11 fc l2
/configure qos ingress-classification-policy "103" dscp af11 profile out
/configure qos ingress-classification-policy "103" dscp af21 fc l1
/configure qos ingress-classification-policy "103" dscp af21 profile out
/configure qos ingress-classification-policy "103" dscp af31 fc l1
/configure qos ingress-classification-policy "103" dscp af31 profile out
/configure qos ingress-classification-policy "103" dscp af32 fc l1
/configure qos ingress-classification-policy "103" dscp af32 profile in
/configure qos ingress-classification-policy "103" dscp af33 fc l1
/configure qos ingress-classification-policy "103" dscp af33 profile in
/configure qos ingress-classification-policy "103" dscp af41 fc h2
/configure qos ingress-classification-policy "103" dscp af41 profile in
/configure qos ingress-classification-policy "103" dscp ef fc ef
/configure qos ingress-classification-policy "103" dscp ef profile in
/configure qos ingress-classification-policy "103" dscp nc2 fc nc
/configure qos ingress-classification-policy "103" dscp nc2 profile in
/configure qos ingress-classification-policy "104" dot1p 0 fc l2
/configure qos ingress-classification-policy "104" dot1p 0 profile out
/configure qos ingress-classification-policy "104" dot1p 3 fc l1
/configure qos ingress-classification-policy "104" dot1p 3 profile out
/configure qos ingress-classification-policy "104" dot1p 4 fc h2
/configure qos ingress-classification-policy "104" dot1p 4 profile out
/configure qos ingress-classification-policy "104" dot1p 5 fc ef
/configure qos ingress-classification-policy "104" dot1p 5 profile out
/configure qos ingress-classification-policy "104" dot1p 6 fc h1
/configure qos ingress-classification-policy "104" dot1p 6 profile out
/configure qos ingress-classification-policy "104" dot1p 7 fc nc
/configure qos ingress-classification-policy "104" dot1p 7 profile out
/configure qos ingress-classification-policy "104" dscp be fc l2
/configure qos ingress-classification-policy "104" dscp be profile out
/configure qos ingress-classification-policy "104" dscp af11 fc l2
/configure qos ingress-classification-policy "104" dscp af11 profile out
/configure qos ingress-classification-policy "104" dscp af21 fc l2
/configure qos ingress-classification-policy "104" dscp af21 profile out
/configure qos ingress-classification-policy "104" dscp af22 fc l1
/configure qos ingress-classification-policy "104" dscp af22 profile out
/configure qos ingress-classification-policy "104" dscp af31 fc l1
/configure qos ingress-classification-policy "104" dscp af31 profile out
/configure qos ingress-classification-policy "104" dscp af41 fc l1
/configure qos ingress-classification-policy "104" dscp af41 profile out
/configure qos ingress-classification-policy "104" dscp af42 fc h2
/configure qos ingress-classification-policy "104" dscp af42 profile in
/configure qos ingress-classification-policy "104" dscp ef fc ef
/configure qos ingress-classification-policy "104" dscp ef profile in
/configure qos ingress-classification-policy "104" dscp nc2 fc h1
/configure qos ingress-classification-policy "104" dscp nc2 profile in
/configure qos ingress-classification-policy "110" description "Real Time VBR QOS"
/configure qos ingress-classification-policy "110" default-action fc h2
/configure qos ingress-classification-policy "110" default-action profile in
/configure qos ingress-classification-policy "120" description "Signalling QOS"
/configure qos ingress-classification-policy "120" default-action fc h1
/configure qos ingress-classification-policy "120" default-action profile in
/configure qos ingress-classification-policy "130" description "Critical Data OP QOS"
/configure qos ingress-classification-policy "130" default-action fc af
/configure qos ingress-classification-policy "140" description "Critical Data IP QOS"
/configure qos ingress-classification-policy "140" default-action fc l1
/configure qos ingress-classification-policy "140" default-action profile in
/configure qos ingress-classification-policy "150" description "Real Time CBR QOS"
/configure qos ingress-classification-policy "150" default-action fc ef
/configure qos ingress-classification-policy "150" default-action profile in
/configure qos ingress-classification-policy "160" description "Network Control QOS"
/configure qos ingress-classification-policy "160" default-action fc nc
/configure qos ingress-classification-policy "160" default-action profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" description "NQ_VFQ_IXR_INGRESS"
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" default-action fc l2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp be fc l2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp be profile out
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af11 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af11 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af12 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af12 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af13 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af13 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs2 fc h1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs2 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af21 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af21 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af22 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af22 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af23 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af23 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs3 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs3 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af31 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af31 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af32 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af32 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af33 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af33 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af41 fc h1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af41 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af42 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp af42 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs5 fc h2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp cs5 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp ef fc ef
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp ef profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp nc1 fc nc
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" dscp nc1 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 0 fc l2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 0 profile out
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 1 fc h2
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 1 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 2 fc h1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 2 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 3 fc af
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 3 profile out
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 4 fc l1
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 4 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 5 fc ef
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 5 profile in
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 6 fc nc
/configure qos ingress-classification-policy "NQ_VFQ_IXR_Ing_class" lsp-exp 6 profile in
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" ingress-classification-policy "NQ_VFQ_IXR_Ing_class"
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 1 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 2 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 3 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 4 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 5 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 6 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 7 stat-mode offered-profile-with-discards
/configure qos network-ingress "NQ_VFQ_IXR_Net_Ing" policer 8 stat-mode offered-profile-with-discards
/configure qos egress-remark-policy "102" description "User Traffic delivered to full IP BTS"
/configure qos egress-remark-policy "102" fc ef dot1p in-profile 6
/configure qos egress-remark-policy "102" fc ef dot1p out-profile 6
/configure qos egress-remark-policy "103" fc l2 dot1p in-profile 0
/configure qos egress-remark-policy "103" fc l2 dot1p out-profile 0
/configure qos egress-remark-policy "103" fc h2 dot1p in-profile 5
/configure qos egress-remark-policy "103" fc h2 dot1p out-profile 5
/configure qos egress-remark-policy "103" fc ef dot1p in-profile 6
/configure qos egress-remark-policy "103" fc ef dot1p out-profile 6
/configure qos egress-remark-policy "103" fc nc dot1p in-profile 0
/configure qos egress-remark-policy "103" fc nc dot1p out-profile 0
/configure qos egress-remark-policy "104" fc l2 dot1p in-profile 0
/configure qos egress-remark-policy "104" fc l2 dot1p out-profile 0
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l2 lsp-exp in-profile 0
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l2 lsp-exp out-profile 0
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc af lsp-exp in-profile 3
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc af lsp-exp out-profile 3
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l1 lsp-exp in-profile 4
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc l1 lsp-exp out-profile 3
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h2 lsp-exp in-profile 1
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h2 lsp-exp out-profile 1
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h1 lsp-exp in-profile 2
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc h1 lsp-exp out-profile 2
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc nc lsp-exp in-profile 6
/configure qos egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" fc nc lsp-exp out-profile 6
/configure router "Base" autonomous-system 48728
/configure router "Base" ecmp 4
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" port {data["port-a1"]}
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" egress qos vlan-qos-policy policy-name "NQ_VFQ_IXR_VLAN_QOS"
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" egress qos egress-remark-policy policy-name "NQ_VFQ_IXR_Eg_Remark"
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" ingress qos network-ingress policy-name "NQ_VFQ_IXR_Net_Ing"
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" ipv4 primary address {data["network-a"]}
/configure router "Base" interface "NET_{data["far-end-a"]}_{data["network-a"]}" ipv4 primary prefix-length 31
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" port {data["port-b1"]}
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" egress qos vlan-qos-policy policy-name "NQ_VFQ_IXR_VLAN_QOS"
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" egress qos egress-remark-policy policy-name "NQ_VFQ_IXR_Eg_Remark"
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" ingress qos network-ingress policy-name "NQ_VFQ_IXR_Net_Ing"
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" ipv4 primary address {data["network-b"]}
/configure router "Base" interface "NET_{data["far-end-b"]}_{data["network-b"]}" ipv4 primary prefix-length 31
/configure router "Base" interface "lbl-bgp-lpbck" loopback
/configure router "Base" interface "lbl-bgp-lpbck" ipv4 primary address {data["loopback"]}
/configure router "Base" interface "lbl-bgp-lpbck" ipv4 primary prefix-length 32
/configure router "Base" interface "system" ipv4 primary address {data["system"]}
/configure router "Base" interface "system" ipv4 primary prefix-length 32
/configure router "Base" bgp min-route-advertisement 5
/configure router "Base" bgp rapid-withdrawal true
/configure router "Base" bgp peer-ip-tracking true
/configure router "Base" bgp ebgp-default-reject-policy import false
/configure router "Base" bgp ebgp-default-reject-policy export false
/configure router "Base" bgp next-hop-resolution labeled-routes transport-tunnel family vpn resolution-filter rsvp true
/configure router "Base" bgp next-hop-resolution labeled-routes transport-tunnel family label-ipv4 resolution-filter rsvp true
/configure router "Base" {{ bgp outbound-route-filtering extended-community send-orf }}
/configure router "Base" bgp group "POC2-lbgp-ipv4" peer-as 48728
/configure router "Base" bgp group "POC2-lbgp-ipv4" family ipv4 true
/configure router "Base" bgp group "POC2-lbgp-ipv4" import policy ["import-from-POC2"]
/configure router "Base" bgp group "POC2-lbgp-ipv4" export policy ["export-to-POC2"]
/configure router "Base" bgp group "Seamless_l3vpns_mp_ibgp" peer-as 48728
/configure router "Base" bgp group "Seamless_l3vpns_mp_ibgp" local-address 192.168.64.111
/configure router "Base" bgp group "Seamless_l3vpns_mp_ibgp" family vpn-ipv4 true
/configure router "Base" bgp neighbor {data["POC2-1"]} group "POC2-lbgp-ipv4"
/configure router "Base" bgp neighbor {data["POC2-1"]} authentication-key VFQatar
/configure router "Base" bgp neighbor {data["POC2-1"]} family label-ipv4 true
/configure router "Base" bgp neighbor {data["POC2-2"]} group "POC2-lbgp-ipv4"
/configure router "Base" bgp neighbor {data["POC2-2"]} authentication-key VFQatar
/configure router "Base" bgp neighbor {data["POC2-2"]} family label-ipv4 true
/configure router "Base" bgp neighbor {data["POC3-1"]} group "Seamless_l3vpns_mp_ibgp"
/configure router "Base" bgp neighbor {data["POC3-2"]} group "Seamless_l3vpns_mp_ibgp"
/configure router "Base" isis 0 admin-state enable
/configure router "Base" isis 0 authentication-key ALU
/configure router "Base" isis 0 authentication-type message-digest
/configure router "Base" isis 0 iid-tlv true
/configure router "Base" isis 0 lsp-lifetime 65535
/configure router "Base" isis 0 traffic-engineering true
/configure router "Base" isis 0 area-address [49.0974]
/configure router "Base" isis 0 timers spf-wait spf-max-wait 2000
/configure router "Base" isis 0 timers spf-wait spf-initial-wait 50
/configure router "Base" isis 0 timers spf-wait spf-second-wait 100
/configure router "Base" isis 0 timers lsp-wait lsp-max-wait 8000
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-key VFQatar
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-type message-digest
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" interface-type point-to-point
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" level-capability 1
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 hello-interval 10
/configure router "Base" isis 0 interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 metric 100
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-key VFQatar
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-type message-digest
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" interface-type point-to-point
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" level-capability 1
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 hello-interval 10
/configure router "Base" isis 0 interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 metric 100
/configure router "Base" {{ isis 0 interface "system" }}
/configure router "Base" isis 0 level 1 wide-metrics-only true
/configure router "Base" isis 0 level 2 wide-metrics-only true
/configure router "Base" isis {data["isis-a-area"]} admin-state enable
/configure router "Base" isis {data["isis-a-area"]} authentication-key ALU
/configure router "Base" isis {data["isis-a-area"]} authentication-type message-digest
/configure router "Base" isis {data["isis-a-area"]} all-l1isis 01:80:c2:00:01:00
/configure router "Base" isis {data["isis-a-area"]} all-l2isis 01:80:c2:00:01:11
/configure router "Base" isis {data["isis-a-area"]} iid-tlv true
/configure router "Base" isis {data["isis-a-area"]} lsp-lifetime 65535
/configure router "Base" isis {data["isis-a-area"]} traffic-engineering true
/configure router "Base" isis {data["isis-a-area"]} area-address [49.0974]
/configure router "Base" isis {data["isis-a-area"]} timers spf-wait spf-max-wait 2000
/configure router "Base" isis {data["isis-a-area"]} timers spf-wait spf-initial-wait 50
/configure router "Base" isis {data["isis-a-area"]} timers spf-wait spf-second-wait 100
/configure router "Base" isis {data["isis-a-area"]} timers lsp-wait lsp-max-wait 8000
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-key VFQatar
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" hello-authentication-type message-digest
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" interface-type point-to-point
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" level-capability 1
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 hello-interval 10
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-a"]}_{data["network-a"]}" level 1 metric 100
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-key VFQatar
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" hello-authentication-type message-digest
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" interface-type point-to-point
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" level-capability 1
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 hello-interval 10
/configure router "Base" isis {data["isis-a-area"]} interface "NET_{data["far-end-b"]}_{data["network-b"]}" level 1 metric 100
/configure router "Base" {{ isis {data["isis-a-area"]} interface "system" }}
/configure router "Base" isis {data["isis-a-area"]} level 1 external-preference 163
/configure router "Base" isis {data["isis-a-area"]} level 1 preference 25
/configure router "Base" isis {data["isis-a-area"]} level 1 wide-metrics-only true
/configure router "Base" {{ ldp interface-parameters interface "NET_{data["far-end-a"]}_{data["network-a"]}" ipv4 }}
/configure router "Base" {{ ldp interface-parameters interface "NET_{data["far-end-b"]}_{data["network-b"]}" ipv4 }}
/configure router "Base" static-routes route 10.100.20.10/31 route-type unicast next-hop {increment_last_octet(data["network-a"])} admin-state enable
/configure router "Base" static-routes route 10.100.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-a"])} admin-state enable
/configure router "Base" static-routes route 10.200.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-a"])} admin-state enable
/configure router "Base" static-routes route 10.100.20.10/31 route-type unicast next-hop {increment_last_octet(data["network-b"])} admin-state enable
/configure router "Base" static-routes route 10.100.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-b"])} admin-state enable
/configure router "Base" static-routes route 10.200.20.64/28 route-type unicast next-hop {increment_last_octet(data["network-b"])} admin-state enable
/configure service vprn "17804" admin-state enable
/configure service vprn "17804" description "eNB IPsec Public eUTRAN VPRN"
/configure service vprn "17804" customer "1"
/configure service vprn "17804" autonomous-system 48728
/configure service vprn "17804" bgp-ipvpn mpls admin-state enable
/configure service vprn "17804" bgp-ipvpn mpls route-distinguisher "48728:17804{data["Site"]}"
/configure service vprn "17804" bgp-ipvpn mpls vrf-target community "target:48728:178040"
/configure service vprn "17804" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17804" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17804" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "17812" admin-state enable
/configure service vprn "17812" description "BTS_BSC_Abis_VPRN"
/configure service vprn "17812" customer "1"
/configure service vprn "17812" autonomous-system 48728
/configure service vprn "17812" bgp-ipvpn mpls admin-state enable
/configure service vprn "17812" bgp-ipvpn mpls route-distinguisher "48728:17812{data["Site"]}"
/configure service vprn "17812" bgp-ipvpn mpls vrf-target community "target:48728:17812"
/configure service vprn "17812" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17812" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17812" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "17813" admin-state enable
/configure service vprn "17813" description "eNB_RNC_IuB_VPRN"
/configure service vprn "17813" customer "1"
/configure service vprn "17813" autonomous-system 48728
/configure service vprn "17813" bgp-ipvpn mpls admin-state enable
/configure service vprn "17813" bgp-ipvpn mpls route-distinguisher "48728:17813{data["Site"]}"
/configure service vprn "17813" bgp-ipvpn mpls vrf-target community "target:48728:17813"
/configure service vprn "17813" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17813" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17813" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "17815" admin-state enable
/configure service vprn "17815" description "Huawei OAM VPRN"
/configure service vprn "17815" customer "1"
/configure service vprn "17815" autonomous-system 48728
/configure service vprn "17815" bgp-ipvpn mpls admin-state enable
/configure service vprn "17815" bgp-ipvpn mpls route-distinguisher "48728:17815{data["Site"]}"
/configure service vprn "17815" bgp-ipvpn mpls vrf-target community "target:48728:17815"
/configure service vprn "17815" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "17815" bgp-ipvpn mpls auto-bind-tunnel resolution-filter ldp true
/configure service vprn "17815" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure service vprn "ENT-4G-5G_Public" description "ENT 4G-5G Public Service"
/configure service vprn "ENT-4G-5G_Public" service-id 55000
/configure service vprn "ENT-4G-5G_Public" customer "1"
/configure service vprn "ENT-4G-5G_Public" autonomous-system 48728
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls admin-state enable
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls route-distinguisher "48728:55000{data["Site"]}"
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls vrf-target community "target:65100:55000"
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls auto-bind-tunnel resolution filter
/configure service vprn "ENT-4G-5G_Public" bgp-ipvpn mpls auto-bind-tunnel resolution-filter rsvp true
/configure system name {data["hostname"]}
/configure system central-frequency-clock ql-selection true
/configure system central-frequency-clock revert true
/configure system central-frequency-clock ref1 admin-state enable
/configure system central-frequency-clock ref1 source-port {data["port-a1"]}
/configure management-interface configuration-mode mixed
/configure management-interface snmp packet-size 9216
/configure management-interface snmp streaming admin-state enable
/configure system security telnet-server true
/configure system security ftp-server true
/configure system security aaa local-profiles profile "ARCH2" default-action deny-all
/configure system security aaa local-profiles profile "ARCH2" entry 1 match "oam"
/configure system security aaa local-profiles profile "ARCH2" entry 1 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 2 match "ping"
/configure system security aaa local-profiles profile "ARCH2" entry 2 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 3 match "admin display-config"
/configure system security aaa local-profiles profile "ARCH2" entry 3 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 4 match "configure port"
/configure system security aaa local-profiles profile "ARCH2" entry 4 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 5 match "telnet"
/configure system security aaa local-profiles profile "ARCH2" entry 5 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 6 match "back"
/configure system security aaa local-profiles profile "ARCH2" entry 6 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 7 match "show"
/configure system security aaa local-profiles profile "ARCH2" entry 7 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 8 match "ssh"
/configure system security aaa local-profiles profile "ARCH2" entry 8 action deny
/configure system security aaa local-profiles profile "ARCH2" entry 9 match "traceroute"
/configure system security aaa local-profiles profile "ARCH2" entry 9 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 10 match "monitor"
/configure system security aaa local-profiles profile "ARCH2" entry 10 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 11 match "admin save"
/configure system security aaa local-profiles profile "ARCH2" entry 11 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 12 match "configure service vprn"
/configure system security aaa local-profiles profile "ARCH2" entry 12 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 13 match "environment more "
/configure system security aaa local-profiles profile "ARCH2" entry 13 action permit
/configure system security aaa local-profiles profile "ARCH2" entry 14 match "info"
/configure system security aaa local-profiles profile "ARCH2" entry 14 action permit
/configure system security aaa local-profiles profile "Monitoring" default-action deny-all
/configure system security aaa local-profiles profile "Monitoring" entry 10 match "exec"
/configure system security aaa local-profiles profile "Monitoring" entry 10 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 20 match "help"
/configure system security aaa local-profiles profile "Monitoring" entry 20 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 30 match "logout"
/configure system security aaa local-profiles profile "Monitoring" entry 30 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 40 match "password"
/configure system security aaa local-profiles profile "Monitoring" entry 40 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 50 match "show"
/configure system security aaa local-profiles profile "Monitoring" entry 50 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 60 match "enable-admin"
/configure system security aaa local-profiles profile "Monitoring" entry 60 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 70 match "configure"
/configure system security aaa local-profiles profile "Monitoring" entry 70 action deny
/configure system security aaa local-profiles profile "Monitoring" entry 80 match "admin display-config"
/configure system security aaa local-profiles profile "Monitoring" entry 80 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 90 match "show config"
/configure system security aaa local-profiles profile "Monitoring" entry 90 action deny
/configure system security aaa local-profiles profile "Monitoring" entry 110 match "traceroute"
/configure system security aaa local-profiles profile "Monitoring" entry 110 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 120 match "exit"
/configure system security aaa local-profiles profile "Monitoring" entry 120 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 130 match "configure li"
/configure system security aaa local-profiles profile "Monitoring" entry 130 action deny
/configure system security aaa local-profiles profile "Monitoring" entry 140 match "ping"
/configure system security aaa local-profiles profile "Monitoring" entry 140 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 150 match "telnet"
/configure system security aaa local-profiles profile "Monitoring" entry 150 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 160 match "monitor port"
/configure system security aaa local-profiles profile "Monitoring" entry 160 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 170 match "monitor lag"
/configure system security aaa local-profiles profile "Monitoring" entry 170 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 180 match "admin save"
/configure system security aaa local-profiles profile "Monitoring" entry 180 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 190 match "admin tech-support"
/configure system security aaa local-profiles profile "Monitoring" entry 190 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 200 match "history"
/configure system security aaa local-profiles profile "Monitoring" entry 200 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 210 match "file"
/configure system security aaa local-profiles profile "Monitoring" entry 210 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 211 match "ssh"
/configure system security aaa local-profiles profile "Monitoring" entry 211 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 212 match "oam lsp-trace"
/configure system security aaa local-profiles profile "Monitoring" entry 212 action permit
/configure system security aaa local-profiles profile "Monitoring" entry 213 match "clear port"
/configure system security aaa local-profiles profile "Monitoring" entry 213 action permit
/configure system security aaa local-profiles profile "NokiaProject" default-action permit-all
/configure system security aaa local-profiles profile "NokiaProject" entry 1 description "reboot"
/configure system security aaa local-profiles profile "NokiaProject" entry 1 match "admin reboot"
/configure system security aaa local-profiles profile "NokiaProject" entry 1 action deny
/configure system security aaa local-profiles profile "NokiaProject" entry 2 description "securty"
/configure system security aaa local-profiles profile "NokiaProject" entry 2 match "configure system security"
/configure system security aaa local-profiles profile "NokiaProject" entry 2 action deny
/configure system security aaa local-profiles profile "Operator" default-action permit-all
/configure system security aaa local-profiles profile "Operator" entry 10 match "configure system security"
/configure system security aaa local-profiles profile "Operator" entry 10 action deny
/configure system security aaa local-profiles profile "Operator" entry 20 match "configure li"
/configure system security aaa local-profiles profile "Operator" entry 20 action deny
/configure system security aaa local-profiles profile "Operator" entry 30 match "show li"
/configure system security aaa local-profiles profile "Operator" entry 30 action deny
/configure system security aaa local-profiles profile "Operator" entry 50 match "configure filter"
/configure system security aaa local-profiles profile "Operator" entry 50 action deny
/configure system security aaa local-profiles profile "SOC" default-action deny-all
/configure system security aaa local-profiles profile "SOC" entry 8 match "configure router interface"
/configure system security aaa local-profiles profile "SOC" entry 8 action permit
/configure system security aaa local-profiles profile "SOC" entry 9 description "Router reboot"
/configure system security aaa local-profiles profile "SOC" entry 9 match "admin reboot"
/configure system security aaa local-profiles profile "SOC" entry 9 action deny
/configure system security aaa local-profiles profile "SOC" entry 20 match "configure router bgp"
/configure system security aaa local-profiles profile "SOC" entry 20 action permit
/configure system security aaa local-profiles profile "SOC" entry 70 match "admin display-config"
/configure system security aaa local-profiles profile "SOC" entry 70 action permit
/configure system security aaa local-profiles profile "SOC" entry 80 match "show"
/configure system security aaa local-profiles profile "SOC" entry 80 action permit
/configure system security aaa local-profiles profile "SOC" entry 90 match "monitor"
/configure system security aaa local-profiles profile "SOC" entry 90 action permit
/configure system security aaa local-profiles profile "SOC" entry 100 match "telnet"
/configure system security aaa local-profiles profile "SOC" entry 100 action permit
/configure system security aaa local-profiles profile "SOC" entry 110 match "ssh"
/configure system security aaa local-profiles profile "SOC" entry 110 action permit
/configure system security aaa local-profiles profile "SOC" entry 120 match "oam"
/configure system security aaa local-profiles profile "SOC" entry 120 action permit
/configure system security aaa local-profiles profile "SOC" entry 140 match "configure router policy-options"
/configure system security aaa local-profiles profile "SOC" entry 140 action permit
/configure system security aaa local-profiles profile "SOC" entry 150 match "configure port"
/configure system security aaa local-profiles profile "SOC" entry 150 action permit
/configure system security aaa local-profiles profile "SOC" entry 160 match "info"
/configure system security aaa local-profiles profile "SOC" entry 160 action permit
/configure system security aaa local-profiles profile "SOC" entry 170 match "ping"
/configure system security aaa local-profiles profile "SOC" entry 170 action permit
/configure system security aaa local-profiles profile "SOC" entry 180 match "traceroute"
/configure system security aaa local-profiles profile "SOC" entry 180 action permit
/configure system security aaa local-profiles profile "SOC" entry 190 match "admin tech-support"
/configure system security aaa local-profiles profile "SOC" entry 190 action permit
/configure system security aaa local-profiles profile "SOC" entry 200 match "history"
/configure system security aaa local-profiles profile "SOC" entry 200 action permit
/configure system security aaa local-profiles profile "SOC" entry 210 match "configure service"
/configure system security aaa local-profiles profile "SOC" entry 210 action permit
/configure system security aaa local-profiles profile "SOC" entry 220 match "exit"
/configure system security aaa local-profiles profile "SOC" entry 220 action permit
/configure system security aaa local-profiles profile "SOC" entry 230 match "admin save"
/configure system security aaa local-profiles profile "SOC" entry 230 action permit
/configure system security aaa local-profiles profile "SOC" entry 240 match "pwc"
/configure system security aaa local-profiles profile "SOC" entry 240 action permit
/configure system security aaa local-profiles profile "SOC" entry 250 match "back"
/configure system security aaa local-profiles profile "SOC" entry 250 action permit
/configure system security aaa local-profiles profile "SOC" entry 260 match "clear"
/configure system security aaa local-profiles profile "SOC" entry 260 action permit
/configure system security aaa local-profiles profile "SOC" entry 270 match "configure lag"
/configure system security aaa local-profiles profile "SOC" entry 270 action permit
/configure system security aaa local-profiles profile "SOC" entry 280 match "configure qos"
/configure system security aaa local-profiles profile "SOC" entry 280 action permit
/configure system security aaa local-profiles profile "SOC" entry 290 match "environment"
/configure system security aaa local-profiles profile "SOC" entry 290 action deny
/configure system security aaa local-profiles profile "TPM" entry 10 match "exec"
/configure system security aaa local-profiles profile "TPM" entry 10 action permit
/configure system security aaa local-profiles profile "TPM" entry 20 match "exit"
/configure system security aaa local-profiles profile "TPM" entry 20 action permit
/configure system security aaa local-profiles profile "TPM" entry 30 match "help"
/configure system security aaa local-profiles profile "TPM" entry 30 action permit
/configure system security aaa local-profiles profile "TPM" entry 40 match "logout"
/configure system security aaa local-profiles profile "TPM" entry 40 action permit
/configure system security aaa local-profiles profile "TPM" entry 41 match "tools dump"
/configure system security aaa local-profiles profile "TPM" entry 41 action permit
/configure system security aaa local-profiles profile "TPM" entry 42 match "sleep"
/configure system security aaa local-profiles profile "TPM" entry 42 action permit
/configure system security aaa local-profiles profile "TPM" entry 43 match "file dir"
/configure system security aaa local-profiles profile "TPM" entry 43 action permit
/configure system security aaa local-profiles profile "TPM" entry 44 match "environment more"
/configure system security aaa local-profiles profile "TPM" entry 44 action permit
/configure system security aaa local-profiles profile "TPM" entry 50 match "password"
/configure system security aaa local-profiles profile "TPM" entry 50 action permit
/configure system security aaa local-profiles profile "TPM" entry 53 match "admin display-config"
/configure system security aaa local-profiles profile "TPM" entry 53 action permit
/configure system security aaa local-profiles profile "TPM" entry 55 match "configure"
/configure system security aaa local-profiles profile "TPM" entry 55 action deny
/configure system security aaa local-profiles profile "TPM" entry 60 match "show config"
/configure system security aaa local-profiles profile "TPM" entry 60 action deny
/configure system security aaa local-profiles profile "TPM" entry 65 match "show li"
/configure system security aaa local-profiles profile "TPM" entry 65 action deny
/configure system security aaa local-profiles profile "TPM" entry 70 match "show"
/configure system security aaa local-profiles profile "TPM" entry 70 action permit
/configure system security aaa local-profiles profile "TPM" entry 80 match "enable-admin"
/configure system security aaa local-profiles profile "TPM" entry 80 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 6 match "monitor"
/configure system security aaa local-profiles profile "VF-NSU" entry 6 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 10 match "exec"
/configure system security aaa local-profiles profile "VF-NSU" entry 10 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 30 match "help"
/configure system security aaa local-profiles profile "VF-NSU" entry 30 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 40 match "logout"
/configure system security aaa local-profiles profile "VF-NSU" entry 40 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 50 match "password"
/configure system security aaa local-profiles profile "VF-NSU" entry 50 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 60 match "admin display-config"
/configure system security aaa local-profiles profile "VF-NSU" entry 60 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 65 match "admin"
/configure system security aaa local-profiles profile "VF-NSU" entry 65 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 70 match "show"
/configure system security aaa local-profiles profile "VF-NSU" entry 70 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 80 match "enable-admin"
/configure system security aaa local-profiles profile "VF-NSU" entry 80 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 100 match "configure"
/configure system security aaa local-profiles profile "VF-NSU" entry 100 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 110 match "tools"
/configure system security aaa local-profiles profile "VF-NSU" entry 110 action deny
/configure system security aaa local-profiles profile "VF-NSU" entry 120 match "ping"
/configure system security aaa local-profiles profile "VF-NSU" entry 120 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 130 match "telnet"
/configure system security aaa local-profiles profile "VF-NSU" entry 130 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 140 match "traceroute"
/configure system security aaa local-profiles profile "VF-NSU" entry 140 action permit
/configure system security aaa local-profiles profile "VF-NSU" entry 150 match "exit"
/configure system security aaa local-profiles profile "VF-NSU" entry 150 action permit
/configure system security {{ aaa local-profiles profile "password" }}
/configure system security aaa local-profiles profile "show" default-action deny-all
/configure system security aaa local-profiles profile "show" entry 1 match "show"
/configure system security aaa local-profiles profile "show" entry 1 action permit
/configure system security aaa local-profiles profile "show" entry 2 match "admin display-config"
/configure system security aaa local-profiles profile "show" entry 2 action permit
/configure system security aaa local-profiles profile "show" entry 7 match "monitor"
/configure system security aaa local-profiles profile "show" entry 7 action permit
/configure system security aaa local-profiles profile "show" entry 8 match "ping"
/configure system security aaa local-profiles profile "show" entry 8 action permit
/configure system security aaa local-profiles profile "show" entry 9 match "telnet"
/configure system security aaa local-profiles profile "show" entry 9 action permit
/configure system security aaa local-profiles profile "tier-1" default-action deny-all
/configure system security aaa local-profiles profile "tier-1" entry 10 match "admin tech-support"
/configure system security aaa local-profiles profile "tier-1" entry 10 action permit
/configure system security aaa local-profiles profile "tier-1" entry 20 match "show"
/configure system security aaa local-profiles profile "tier-1" entry 20 action permit
/configure system security aaa local-profiles profile "tier-1" entry 30 match "exit"
/configure system security aaa local-profiles profile "tier-1" entry 30 action permit
/configure system security snmp access "nmsPriv" context "" security-model usm security-level privacy read "iso"
/configure system security snmp access "nmsPriv" context "" security-model usm security-level privacy write "iso"
/configure system security snmp access "nmsPriv" context "" security-model usm security-level privacy notify "iso"
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy prefix-match prefix
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy read "vprn-view"
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy write "vprn-view"
/configure system security snmp access "nmsPriv" context "vprn" security-model usm security-level privacy notify "iso"
/configure system security snmp community "76HzdddhlPpRo1Vql+ZB5spLqccgYQ== hash2" access-permissions r
/configure system security snmp community "76HzdddhlPpRo1Vql+ZB5spLqccgYQ== hash2" version v2c
/configure system security user-params local-user password complexity-rules required lowercase 1
/configure system security user-params local-user password complexity-rules required uppercase 1
/configure system security user-params local-user password complexity-rules required numeric 1
/configure system security user-params local-user password complexity-rules required special-character 1
/configure system security user-params local-user user "AdminSAM5620" password "$2y$10$QGGVBkdQhc.V9ceWwfl6..ynxeadOnjPSgFRiAXwGQa3pLGZsN7PK"
/configure system security user-params local-user user "AdminSAM5620" access console true
/configure system security user-params local-user user "AdminSAM5620" access ftp true
/configure system security user-params local-user user "AdminSAM5620" access snmp true
/configure system security user-params local-user user "AdminSAM5620" console member ["default" "administrative"]
/configure system security {{ user-params local-user user "AdminSAM5620" snmp authentication }}
/configure system security user-params local-user user "VFQ.arajeeb" password "$2y$10$.ITViSWCVNkgClQNo9TMY.3zg.gBQZCLjjNRY1WhIy.GkN8eC/6dy"
/configure system security user-params local-user user "VFQ.arajeeb" access console true
/configure system security user-params local-user user "VFQ.arajeeb" access ftp true
/configure system security user-params local-user user "VFQ.arajeeb" console member ["default" "Operator"]
/configure system security user-params local-user user "admin" password "$2y$10$lnMYTNLh3YK1G5e6bCzlg.hcCfnMQdu9HShe6CNxbUW3Li6Eazq4K"
/configure system security user-params local-user user "admin" access console true
/configure system security user-params local-user user "admin" access ftp true
/configure system security user-params local-user user "admin" access netconf true
/configure system security user-params local-user user "admin" access grpc true
/configure system security user-params local-user user "admin" console member ["administrative"]
/configure system security user-params local-user user "admin" public-keys ecdsa ecdsa-key 32 key-value "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIr3f6WDgc4OPwnTzCWQuzbDjMbhg+9Vnnlu5Wp2Wc5TLF4xQslbJVAxR38EYkJ5GZWoyvBktxa0NuQ5MxCZBqs="
/configure system security user-params local-user user "ameers" password "$2y$10$NMjfPL4Kauf1seZOSPcKc./9vc3JrMdoSF0HJlh8GS.kAmTCJHeVO"
/configure system security user-params local-user user "ameers" access console true
/configure system security user-params local-user user "ameers" access ftp true
/configure system security user-params local-user user "ameers" access snmp true
/configure system security user-params local-user user "ameers" console member ["default" "NokiaProject"]
/configure system security user-params local-user user "amogh.acharya" password "$2y$10$l2fFGhaiiVE8f0E5mYe62.L5RYheC6Xn1r6UcmiiOMqw5MskjRjqa"
/configure system security user-params local-user user "amogh.acharya" access console true
/configure system security user-params local-user user "amogh.acharya" console member ["default" "Operator"]
/configure system security user-params local-user user "anas.hammami" password "$2y$10$4UStCMbBpydY2jsaEcj9o./b49aloC0qZo7kgdgOXnRXz2jDFsKeW"
/configure system security user-params local-user user "anas.hammami" access console true
/configure system security user-params local-user user "anas.hammami" access ftp true
/configure system security user-params local-user user "anas.hammami" console member ["administrative"]
/configure system security user-params local-user user "chrisnanda.ent" password "$2y$10$/YtllkeV45TIzAFlkw0Ks.ZOxXjkhrbELh.ZSgivB0oan4lQMheje"
/configure system security user-params local-user user "chrisnanda.ent" access console true
/configure system security user-params local-user user "chrisnanda.ent" access ftp true
/configure system security user-params local-user user "chrisnanda.ent" console member ["default" "administrative"]
/configure system security user-params local-user user "deni.sartika" password "$2y$10$GPYPa.WMxyxF7TW79K09g.Y0FrP.C7HtIAPVGl8EltTGdPKDn/pi."
/configure system security user-params local-user user "deni.sartika" access console true
/configure system security user-params local-user user "deni.sartika" access ftp true
/configure system security user-params local-user user "deni.sartika" console member ["administrative"]
/configure system security user-params local-user user "gems.bo" password "$2y$10$tc0o3pEKR3en89sgtk2b2.KC9rwkw5L6pKvfF95n6787vowCmwUzm"
/configure system security user-params local-user user "gems.bo" access console true
/configure system security user-params local-user user "gems.bo" access ftp true
/configure system security user-params local-user user "gems.bo" console member ["default" "Operator"]
/configure system security user-params local-user user "gnocipfo" password "$2y$10$R7ZyDzV9J57tOW/Z3AX9..y0t/PdvBNWEo26.VcWDy77haJOjJHi6"
/configure system security user-params local-user user "gnocipfo" access console true
/configure system security user-params local-user user "gnocipfo" access ftp true
/configure system security user-params local-user user "gnocipfo" access snmp true
/configure system security user-params local-user user "gnocipfo" console member ["default" "show"]
/configure system security {{ user-params local-user user "gnocipfo" snmp authentication }}
/configure system security user-params local-user user "muhammad.ehsan" password "$2y$10$Sja5NHyihHEh1hvbMhHdo.ftFhjP1l7cXXMtVOB.dmlyP4EHcRscC"
/configure system security user-params local-user user "muhammad.ehsan" access console true
/configure system security user-params local-user user "muhammad.ehsan" access ftp true
/configure system security user-params local-user user "muhammad.ehsan" console member ["default" "Operator" "administrative"]
/configure system security user-params local-user user "rohitb" password "$2y$10$eyQrBfoT8Gi4XEd1EJexM.EHxOeBBzMlfBf/gVNZ3Ui2DqlocvXjS"
/configure system security user-params local-user user "rohitb" access console true
/configure system security user-params local-user user "rohitb" access ftp true
/configure system security user-params local-user user "rohitb" console member ["default" "administrative"]
/configure system security user-params local-user user "samcli" password "$2y$10$N5URo5oH0xQ7HBdxK1ms2.kgWEGE5xp0c96vhCEQ.bltHKykRIJe6"
/configure system security user-params local-user user "samcli" access console true
/configure system security user-params local-user user "samcli" console member ["administrative"]
/configure system security user-params local-user user "snmpv3user" password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
/configure system security user-params local-user user "snmpv3user" access snmp true
/configure system security user-params local-user user "snmpv3user" console member ["default"]
/configure system security user-params local-user user "snmpv3user" snmp group "nmsPriv"
/configure system security user-params local-user user "snmpv3user" snmp authentication authentication-protocol hmac-sha1-96
/configure system security user-params local-user user "snmpv3user" snmp authentication authentication-key "vzCgV2ozcprrQwCl/rp+bOe2SGtnkRuD4c0t0y6A7bY7LLkA hash2"
/configure system security user-params local-user user "snmpv3user" snmp authentication privacy privacy-protocol cbc-des
/configure system security user-params local-user user "snmpv3user" snmp authentication privacy privacy-key "supXCSZYiL+Ugo6/Jjb4tm5crAKmHOw35sP+EbMiAFc= hash2"
/configure system security user-params local-user user "vfq.mali" password "$2y$10$zhkSzfGw6ET8iTy7ZDxeA.4vlfqyNbfnl942oWLydTWFGHJ6t2enu"
/configure system security user-params local-user user "vfq.mali" access console true
/configure system security user-params local-user user "vfq.mali" access ftp true
/configure system security user-params local-user user "vfq.mali" console member ["default" "administrative"]
/configure system time ntp server 10.100.20.68 router-instance "Base" prefer true
/configure system time {{ ntp server 10.200.20.68 router-instance "Base" }}
/configure system time {{ ntp server 172.16.240.41 router-instance "Base" }}
/edit-config bof private
/bof configuration primary-location "cf3" / {data["hostname"]}.cfg"
/bof system persistent-indices true
commit
quit-config
"""
    return (txt)
