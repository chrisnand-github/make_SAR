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

def make_route_base_IXR_small (data):
    txt=f"""
exit all
configure
#--------------------------------------------------
echo "System Configuration"
#--------------------------------------------------
    system
        name {data["hostname"]}
        management-interface
            cli
                md-cli
                    no auto-config-save
                exit
            exit
            yang-modules
                no nokia-combined-modules
                nokia-submodules
            exit
        exit
        netconf
            shutdown
            no auto-config-save
        exit
        snmp
            streaming
                no shutdown
            exit
            packet-size 9216
        exit
        time
            ntp
                no authentication-check
                no shutdown
            exit
            sntp
                shutdown
            exit
            zone MSK
        exit
        thresholds
            rmon
                alarm 10 variable-oid sgiCpuUsage.0 interval 5 rising-event 10 rising-threshold 80
                event 10 description "CPU utilization is over 80%"
            exit
        exit
    exit
#--------------------------------------------------
echo "System Security Configuration"
#--------------------------------------------------
   system
        security
            telnet-server
            ftp-server
            profile "SOC"
                default-action deny-all
                entry 8
                    match "configure router interface"
                    action permit
                exit
                entry 9
                    description "Router reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 20
                    match "configure router bgp"
                    action permit
                exit
                entry 70
                    match "admin display-config"
                    action permit
                exit
                entry 80
                    match "show"
                    action permit
                exit
                entry 90
                    match "monitor"
                    action permit
                exit
                entry 100
                    match "telnet"
                    action permit
                exit
                entry 110
                    match "ssh"
                    action permit
                exit
                entry 120
                    match "oam"
                    action permit
                exit
                entry 140
                    match "configure router policy-options"
                    action permit
                exit
                entry 150
                    match "configure port"
                    action permit
                exit
                entry 160
                    match "info"
                    action permit
                exit
                entry 170
                    match "ping"
                    action permit
                exit
                entry 180
                    match "traceroute"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "configure service"
                    action permit
                exit
                entry 220
                    match "exit"
                    action permit
                exit
                entry 230
                    match "admin save"
                    action permit
                exit
                entry 240
                    match "pwc"
                    action permit
                exit
                entry 250
                    match "back"
                    action permit
                exit
                entry 260
                    match "clear"
                    action permit
                exit
                entry 270
                    match "configure lag"
                    action permit
                exit
                entry 280
                    match "configure qos"
                    action permit
                exit
                entry 290
                    match "environment"
                    action deny
                exit
            exit
            profile "TPM"
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "exit"
                    action permit
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 41
                    match "tools dump"
                    action permit
                exit
                entry 42
                    match "sleep"
                    action permit
                exit
                entry 43
                    match "file dir"
                    action permit
                exit
                entry 44
                    match "environment more"
                    action permit
                exit
                entry 50
                    match "password"
                    action permit
                exit
                entry 53
                    match "admin display-config"
                    action permit
                exit
                entry 55
                    match "configure"
                    action deny
                exit
                entry 60
                    match "show config"
                    action deny
                exit
                entry 65
                    match "show li"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action permit
                exit
            exit
            profile "show"
                default-action deny-all
                entry 1
                    match "show"
                    action permit
                exit
                entry 2
                    match "admin display-config"
                    action permit
                exit
                entry 7
                    match "monitor"
                    action permit
                exit
                entry 8
                    match "ping"
                    action permit
                exit
                entry 9
                    match "telnet"
                    action permit
                exit
            exit
            profile "ARCH2"
                default-action deny-all
                entry 1
                    match "oam"
                    action permit
                exit
                entry 2
                    match "ping"
                    action permit
                exit
                entry 3
                    match "admin display-config"
                    action permit
                exit
                entry 4
                    match "configure port"
                    action permit
                exit
                entry 5
                    match "telnet"
                    action permit
                exit
                entry 6
                    match "back"
                    action permit
                exit
                entry 7
                    match "show"
                    action permit
                exit
                entry 8
                    match "ssh"
                    action deny
                exit
                entry 9
                    match "traceroute"
                    action permit
                exit
                entry 10
                    match "monitor"
                    action permit
                exit
                entry 11
                    match "admin save"
                    action permit
                exit
                entry 12
                    match "configure service vprn"
                    action permit
                exit
                entry 13
                    match "environment more "
                    action permit
                exit
                entry 14
                    match "info"
                    action permit
                exit
            exit
            profile "VF-NSU"
                entry 6
                    match "monitor"
                    action permit
                exit
                entry 10
                    match "exec"
                    action deny
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 50
                    match "password"
                    action deny
                exit
                entry 60
                    match "admin display-config"
                    action permit
                exit
                entry 65
                    match "admin"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action deny
                exit
                entry 100
                    match "configure"
                    action deny
                exit
                entry 110
                    match "tools"
                    action deny
                exit
                entry 120
                    match "ping"
                    action permit
                exit
                entry 130
                    match "telnet"
                    action permit
                exit
                entry 140
                    match "traceroute"
                    action permit
                exit
                entry 150
                    match "exit"
                    action permit
                exit
            exit
            profile "tier-1"
                default-action deny-all
                entry 10
                    match "admin tech-support"
                    action permit
                exit
                entry 20
                    match "show"
                    action permit
                exit
                entry 30
                    match "exit"
                    action permit
                exit
            exit
            profile "Operator"
                default-action permit-all
                entry 10
                    match "configure system security"
                    action deny
                exit
                entry 20
                    match "configure li"
                    action deny
                exit
                entry 30
                    match "show li"
                    action deny
                exit
                entry 50
                    match "configure filter"
                    action deny
                exit
            exit
            profile "password"
            exit
            profile "Monitoring"
                default-action deny-all
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "help"
                    action permit
                exit
                entry 30
                    match "logout"
                    action permit
                exit
                entry 40
                    match "password"
                    action permit
                exit
                entry 50
                    match "show"
                    action permit
                exit
                entry 60
                    match "enable-admin"
                    action permit
                exit
                entry 70
                    match "configure"
                    action deny
                exit
                entry 80
                    match "admin display-config"
                    action permit
                exit
                entry 90
                    match "show config"
                    action deny
                exit
                entry 110
                    match "traceroute"
                    action permit
                exit
                entry 120
                    match "exit"
                    action permit
                exit
                entry 130
                    match "configure li"
                    action deny
                exit
                entry 140
                    match "ping"
                    action permit
                exit
                entry 150
                    match "telnet"
                    action permit
                exit
                entry 160
                    match "monitor port"
                    action permit
                exit
                entry 170
                    match "monitor lag"
                    action permit
                exit
                entry 180
                    match "admin save"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "file"
                    action permit
                exit
                entry 211
                    match "ssh"
                    action permit
                exit
                entry 212
                    match "oam lsp-trace"
                    action permit
                exit
                entry 213
                    match "clear port"
                    action permit
                exit
            exit
            profile "NokiaProject"
                default-action permit-all
                entry 1
                    description "reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 2
                    description "securty"
                    match "configure system security"
                    action deny
                exit
            exit
            password
                authentication-order local tacplus radius
                complexity-rules
                    required lowercase 1 uppercase 1 numeric 1 special-character 1
                exit
            exit
            user "AdminSAM5620"
                password "$2y$10$QGGVBkdQhc.V9ceWwfl6..ynxeadOnjPSgFRiAXwGQa3pLGZsN7PK"
                access console ftp snmp 
                console
                    member "default"
                    member "administrative"
                exit
                snmp
                    authentication none
                exit
            exit
            user "admin"
                password "$2y$10$lnMYTNLh3YK1G5e6bCzlg.hcCfnMQdu9HShe6CNxbUW3Li6Eazq4K"
                access console ftp 
                console
                    member "administrative"
                exit
            exit
            user "ameers"
                password "$2y$10$NMjfPL4Kauf1seZOSPcKc./9vc3JrMdoSF0HJlh8GS.kAmTCJHeVO"
                access console ftp snmp 
                console
                    member "default"
                    member "NokiaProject"
                exit
            exit
            user "chrisnanda.ent"
                password "$2y$10$/YtllkeV45TIzAFlkw0Ks.ZOxXjkhrbELh.ZSgivB0oan4lQMheje"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "gnocipfo"
                password "$2y$10$R7ZyDzV9J57tOW/Z3AX9..y0t/PdvBNWEo26.VcWDy77haJOjJHi6"
                access console ftp snmp 
                console
                    member "default"
                    member "show"
                exit
                snmp
                    authentication none
                exit
            exit
            user "samcli"
                password "$2y$10$N5URo5oH0xQ7HBdxK1ms2.kgWEGE5xp0c96vhCEQ.bltHKykRIJe6"
                access console 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "snmpv3user"
                password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
                access snmp 
                snmp
                    authentication hmac-sha1-96 344277c1f4fd287c29f2783ee03567513a99575a privacy cbc-des 344277c1f4fd287c29f2783ee0356751
                    group "nmsPriv"
                exit
            exit
            user "muhammad.ehsan"
                password "$2y$10$Sja5NHyihHEh1hvbMhHdo.ftFhjP1l7cXXMtVOB.dmlyP4EHcRscC"
                access console ftp
                console
                    member "Operator"
                    member "administrative"
                exit
            exit
            user "rohitb"
                password "$2y$10$eyQrBfoT8Gi4XEd1EJexM.EHxOeBBzMlfBf/gVNZ3Ui2DqlocvXjS"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "anas.hammami"
                password "$2y$10$4UStCMbBpydY2jsaEcj9o./b49aloC0qZo7kgdgOXnRXz2jDFsKeW"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "vfq.mali"
                password "$2y$10$zhkSzfGw6ET8iTy7ZDxeA.4vlfqyNbfnl942oWLydTWFGHJ6t2enu"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "deni.sartika"
                password "$2y$10$GPYPa.WMxyxF7TW79K09g.Y0FrP.C7HtIAPVGl8EltTGdPKDn/pi."
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "amogh.acharya"
                password "$2y$10$l2fFGhaiiVE8f0E5mYe62.L5RYheC6Xn1r6UcmiiOMqw5MskjRjqa"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "gems.bo"
                password "$2y$10$tc0o3pEKR3en89sgtk2b2.KC9rwkw5L6pKvfF95n6787vowCmwUzm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.arajeeb"
                password "$2y$10$.ITViSWCVNkgClQNo9TMY.3zg.gBQZCLjjNRY1WhIy.GkN8eC/6dy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            snmp
                access group "nmsPriv" security-model usm security-level privacy read "iso" write "iso" notify "iso"
                access group "nmsPriv" security-model usm security-level privacy context "vprn" prefix read "vprn-view" write "vprn-view" notify "iso"
            exit
        exit
    exit
#--------------------------------------------------
echo "System Login Control Configuration"
#--------------------------------------------------
    system
        login-control
            telnet
                inbound-max-sessions 10
                outbound-max-sessions 10
            exit
            idle-timeout 180
        exit
    exit
#--------------------------------------------------
echo "Log Configuration"
#--------------------------------------------------
    log
        file-id 9 name "9"
            location cf3:
            rollover 2880 retention 500
        exit
        file-id 27 name "27"
            description "SAP drop collection"
            location cf3:
            rollover 15 retention 4
        exit
        file-id 38 name "38"
            description "MBH"
            location cf3:
            rollover 15 retention 4
        exit
        file-id 95 name "95"
            description "Main Log File"
            location cf3:
            rollover 360 retention 72
        exit
        accounting-policy 27
            description "MBH drop statistic collection"
            record service-egress-packets
            collection-interval 15
            to file 27
            no shutdown
        exit
        accounting-policy 28
            description "MBH Drop collection"
            record service-ingress-packets
            collection-interval 15
            to file 38
            no shutdown
        exit
        event-control "system" 2103 generate
        event-control "system" 2104 generate
        event-control "vrtr" 2034 generate
        snmp-trap-group 98 name "98"
            description "5620sam"
            trap-target "10.100.16.132:162" address 10.100.16.132 snmpv2c notify-community "citrix"
            trap-target "10.100.20.68:162" address 10.100.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "10.200.20.68:162" address 10.200.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "D89D672883B8:main1" address 10.200.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
            trap-target "D89D672883B8:main2" address 10.100.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
        exit
        log-id 9 name "9"
            time-format local
            from change
            to file 9
            no shutdown
        exit
        log-id 14 name "14"
            from debug-trace
            to memory
            no shutdown
        exit
        log-id 20 name "20"
            from debug-trace
            no shutdown
        exit
        log-id 95 name "95"
            from main
            to file 95
            no shutdown
        exit
        log-id 98 name "98"
            from main security change
            to snmp 1024
            no shutdown
        exit
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        queue-mgmt-policy "QM_104_12500" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q1" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q2" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q3" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 9380
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q4" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 9380
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q5" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 10
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q6" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 10
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q7" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 2500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q8" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 2500
        exit
        port-qos-policy "NQ_VFQ_IXR_PORT_QOS" create
            description "IXR Network QoS"
            queue "1" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
            exit
            queue "2" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
            exit
            queue "3" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
                scheduler-mode wfq
                    percent-rate 100.00 cir 80.00
                exit
            exit
            queue "4" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
                scheduler-mode wfq
                    percent-rate 100.00 cir 80.00
                exit
            exit
            queue "5" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
                scheduler-mode wfq
                    percent-rate 10.00 cir 10.00
                exit
            exit
            queue "6" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
                scheduler-mode wfq
                    percent-rate 100.00 cir 100.00
                exit
            exit
            queue "7" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
                scheduler-mode wfq
                    percent-rate 100.00 cir 10.00
                exit
            exit
            queue "8" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
                scheduler-mode wfq
                    percent-rate 100.00 cir 20.00
                exit
            exit
        exit
        vlan-qos-policy "102" create
            description "Egress for 2G full IP"
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "103" create
            description "User Traffic delivered to full IP nodeB"
            queue "3" create
                percent-rate 100.00 cir 100.00
            exit
            queue "4" create
                percent-rate 100.00 cir 100.00
            exit
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
                queue-type expedite-hi
                exit
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "104" create
            description "4G LTE SAP Egress policy"
            queue "1" create
                queue-mgmt "QM_104_12500"
            exit
            queue "2" create
                queue-mgmt "QM_104_12500"
            exit
            queue "3" create
                queue-mgmt "QM_104_12500"
            exit
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
            exit
            queue "7" create
                percent-rate 100.00 cir 100.00
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" create
            description "IXR Network QoS"
            queue "1" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
            exit
            queue "2" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
            exit
            queue "3" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
                percent-rate 100.00 cir 80.00
            exit
            queue "4" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
                percent-rate 100.00 cir 80.00
            exit
            queue "5" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
                percent-rate 10.00 cir 10.00
            exit
            queue "6" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
                percent-rate 100.00 cir 100.00
            exit
            queue "7" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
                percent-rate 100.00 cir 10.00
            exit
            queue "8" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
                percent-rate 100.00 cir 20.00
            exit
        exit
        egress-remark-policy "102" create
            description "User Traffic delivered to full IP BTS"
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 6 out-profile 6
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 1 out-profile 1
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
            exit
        exit
        egress-remark-policy "103" create
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 6 out-profile 6
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 5 out-profile 5
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 0 out-profile 0
            exit
        exit
        egress-remark-policy "104" create
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 5 out-profile 5
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
            exit
        exit
        egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" create
            fc af create
                dot1p in-profile 2 out-profile 2
                lsp-exp in-profile 3 out-profile 3
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 5 out-profile 5
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
                lsp-exp in-profile 2 out-profile 2
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
                lsp-exp in-profile 1 out-profile 1
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
                lsp-exp in-profile 4 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 1 out-profile 1
                lsp-exp in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
                lsp-exp in-profile 6 out-profile 6
            exit
        exit
        ingress-classification-policy "100" create
            description "Standard QOS"
            default-action fc "l2"
        exit
        ingress-classification-policy "102" create
            dot1p 1 fc "l2" profile out
            dot1p 3 fc "l1" profile out
            dot1p 4 fc "h2"
            dot1p 6 fc "ef"
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "af11" fc "l2" profile out
            dscp "af31" fc "l1" profile out
            dscp "af41" fc "h2"
        exit
        ingress-classification-policy "103" create
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "nc2" fc "nc"
            dscp "af11" fc "l2" profile out
            dscp "af21" fc "l1" profile out
            dscp "af31" fc "l1" profile out
            dscp "af32" fc "l1"
            dscp "af33" fc "l1"
            dscp "af41" fc "h2"
        exit
        ingress-classification-policy "104" create
            dot1p 0 fc "l2" profile out
            dot1p 3 fc "l1" profile out
            dot1p 4 fc "h2" profile out
            dot1p 5 fc "ef" profile out
            dot1p 6 fc "h1" profile out
            dot1p 7 fc "nc" profile out
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "nc2" fc "h1"
            dscp "af11" fc "l2" profile out
            dscp "af21" fc "l2" profile out
            dscp "af22" fc "l1" profile out
            dscp "af31" fc "l1" profile out
            dscp "af41" fc "l1" profile out
            dscp "af42" fc "h2"
        exit
        ingress-classification-policy "110" create
            description "Real Time VBR QOS"
            default-action fc "h2" profile in
        exit
        ingress-classification-policy "120" create
            description "Signalling QOS"
            default-action fc "h1" profile in
        exit
        ingress-classification-policy "130" create
            description "Critical Data OP QOS"
            default-action fc "af"
        exit
        ingress-classification-policy "140" create
            description "Critical Data IP QOS"
            default-action fc "l1" profile in
        exit
        ingress-classification-policy "150" create
            description "Real Time CBR QOS"
            default-action fc "ef" profile in
        exit
        ingress-classification-policy "160" create
            description "Network Control QOS"
            default-action fc "nc" profile in
        exit
        ingress-classification-policy "NQ_VFQ_IXR_Ing_class" create
            description "NQ_VFQ_IXR_INGRESS"
            default-action fc "l2"
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "cs2" fc "h1"
            dscp "cs3" fc "l1"
            dscp "cs5" fc "h2"
            dscp "nc1" fc "nc"
            dscp "af11" fc "l1"
            dscp "af12" fc "l1"
            dscp "af13" fc "l1"
            dscp "af21" fc "l1"
            dscp "af22" fc "l1"
            dscp "af23" fc "l1"
            dscp "af31" fc "l1"
            dscp "af32" fc "l1"
            dscp "af33" fc "l1"
            dscp "af41" fc "h1"
            dscp "af42" fc "l1"
            lsp-exp 0 fc "l2" profile out
            lsp-exp 1 fc "h2"
            lsp-exp 2 fc "h1"
            lsp-exp 3 fc "af" profile out
            lsp-exp 4 fc "l1"
            lsp-exp 5 fc "ef"
            lsp-exp 6 fc "nc"
        exit
        network-ingress "NQ_VFQ_IXR_Net_Ing" create
            ingress-classification-policy "NQ_VFQ_IXR_Ing_class"
            policer 1
                stat-mode offered-profile-with-discards
            exit
            policer 2
                stat-mode offered-profile-with-discards
            exit
            policer 3
                stat-mode offered-profile-with-discards
            exit
            policer 4
                stat-mode offered-profile-with-discards
            exit
            policer 5
                stat-mode offered-profile-with-discards
            exit
            policer 6
                stat-mode offered-profile-with-discards
            exit
            policer 7
                stat-mode offered-profile-with-discards
            exit
            policer 8
                stat-mode offered-profile-with-discards
            exit
            fc af
                policer 3
            exit
            fc be
                policer 1
            exit
            fc ef
                policer 6
            exit
            fc h1
                policer 7
            exit
            fc h2
                policer 5
            exit
            fc l1
                policer 4
            exit
            fc l2
                policer 2
            exit
            fc nc
                policer 8
            exit
        exit
    exit
#--------------------------------------------------
echo "Oper-Groups (Declarations) Configuration"
#--------------------------------------------------
    service
    exit
#--------------------------------------------------
echo "Card Configuration"
#--------------------------------------------------
    card 1
        card-type imm14-10g-sfp++4-1g-tx
        mda 1
            sync-e
            no shutdown
        exit
        no shutdown
    exit
#--------------------------------------------------
echo "Port Configuration"
#--------------------------------------------------
    port {data["port-a1"]}
        description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
        ethernet
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    port {data["port-b1"]}
        description "NET_{data["hostname"]}:{data["port-b1"]}:NET_{data["far-end-b"]}:{data["port-b2"]}:{data["port-b-type"]}:10GE"
        ethernet
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    port A/1
    exit
#--------------------------------------------------
echo "System Sync-If-Timing Configuration"
#--------------------------------------------------
    system
        sync-if-timing
            begin
            ql-selection
            ref1
                source-port {data["port-a1"]}
                no shutdown
            exit
            revert
            commit
        exit
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        sap-ingress 102 name "102" create
            description "Ingress for 2G full IP"
            ingress-classification-policy "102"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
                rate max cir 100
            exit
            policer 4 create
                rate max cir 100
            exit
            policer 5 create
                rate max cir max
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 103 name "103" create
            ingress-classification-policy "103"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
                rate max cir 100
            exit
            policer 4 create
                rate max cir 100
            exit
            policer 5 create
                rate max cir max
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 104 name "104" create
            description "4G LTE SAP Ingress policy"
            ingress-classification-policy "104"
            policer 1 create
                stat-mode offered-profile-with-discards
                mbs 12500 kilobytes
                cbs 6250 kilobytes
            exit
            policer 2 create
                stat-mode offered-profile-with-discards
                mbs 12500 kilobytes
                cbs 6250 kilobytes
            exit
            policer 3 create
                stat-mode offered-profile-with-discards
            exit
            policer 4 create
                stat-mode offered-profile-with-discards
            exit
            policer 5 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 6 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 7 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 8 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 110 name "110" create
            description "Real Time VBR QOS"
            ingress-classification-policy "110"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 120 name "120" create
            description "Signalling QOS"
            ingress-classification-policy "120"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
                rate max cir max
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 130 name "130" create
            description "Critical Data OP QOS"
            ingress-classification-policy "130"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 140 name "140" create
            description "Critical Data IP QOS"
            ingress-classification-policy "140"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 150 name "150" create
            description "Real Time CBR QOS"
            ingress-classification-policy "150"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 160 name "160" create
            description "Network Control QOS"
            ingress-classification-policy "160"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
    exit
#--------------------------------------------------
echo "Management Router Configuration"
#--------------------------------------------------
    router management
    exit

#--------------------------------------------------
echo "Router (Network Side) Configuration"
#--------------------------------------------------
    router Base
        interface "NET_{data["far-end-a"]}_{data["network-a"]}"
            address {data["network-a"]}/31
            egress
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            port {data["port-a1"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
            exit
            no shutdown
        exit
        interface "NET_{data["far-end-b"]}_{data["network-b"]}"
            address {data["network-b"]}/31
            egress
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            port {data["port-a1"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
            exit
            no shutdown
        exit
        interface "lbl-bgp-lpbck"
            address {data["loopback"]}/32
            loopback
            ingress
            exit
            no shutdown
        exit
        interface "system"
            address {data["system"]}/32
            no shutdown
        exit
        autonomous-system 48728
        ecmp 4
#--------------------------------------------------
echo "Static Route Configuration"
#--------------------------------------------------
        static-route-entry 10.100.20.10/31
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
        static-route-entry 10.100.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
        static-route-entry 10.200.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                wide-metrics-only
            exit
            level 2
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            interface "NET_{data["far-end-b"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            all-l1isis 01:80:c2:00:01:00
            all-l2isis 01:80:c2:00:01:11
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                external-preference 163
                preference 25
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            interface "NET_{data["far-end-b"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "LDP Configuration"
#--------------------------------------------------
        ldp
            import-pmsi-routes
            exit
            tcp-session-parameters
            exit
            interface-parameters
                interface "NET_{data["far-end-a"]}_{data["network-a"]}"  dual-stack
                    ipv4
                        no shutdown
                    exit
                    no shutdown
                exit
                interface "NET_{data["far-end-b"]}_{data["network-b"]}"  dual-stack
                    ipv4
                        no shutdown
                    exit
                    no shutdown
                exit
            exit
            targeted-session
            exit
            no shutdown
        exit
    exit

#--------------------------------------------------
echo "Service Configuration"
#--------------------------------------------------
    service
        vprn 17804 customer 1 create
            description "eNB IPsec Public eUTRAN VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17804{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:178040
            no shutdown
        exit
        vprn 17812 customer 1 create
            description "BTS_BSC_Abis_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17812{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17812
            no shutdown
        exit
        vprn 17813 customer 1 create
            description "eNB_RNC_IuB_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17813{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17813
            no shutdown
        exit
        vprn 17815 customer 1 create
            description "Huawei OAM VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17815{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17815
            no shutdown
        exit
        vprn 55000 name "ENT-4G-5G_Public" customer 1 create
            description "ENT 4G-5G Public Service"
            autonomous-system 48728
            route-distinguisher 48728:55000{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:65100:55000
            no shutdown
        exit
    exit
#--------------------------------------------------
echo "Router (Service Side) Configuration"
#--------------------------------------------------
    router Base
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            no shutdown
        exit
#--------------------------------------------------
echo "Policy Configuration"
#--------------------------------------------------
        policy-options
            begin
            prefix-list "lbl-bgp-lpbck"
                prefix {data["loopback"]}/32 exact
            exit
            prefix-list "only-lbl-bgp-lpbcks"
                prefix 192.168.64.0/20 prefix-length-range 32-32
            exit
            community "service-lpbcks-IS0"
                members "48728:1110"
            exit
            community "service-lpbcks-IS1"
                members "48728:1111"
            exit
            community "service-lpbcks-IS2"
                members "48728:1112"
            exit
            community "service-lpbcks-IS3"
                members "48728:1113"
            exit
            community "service-lpbcks-IS4"
                members "48728:1114"
            exit
            community "service-lpbcks-IS5"
                members "48728:1115"
            exit
            community "service-lpbcks-IS6"
                members "48728:1116"
            exit
            community "service-lpbcks-IS7"
                members "48728:1117"
            exit
            community "service-lpbcks-IS8"
                members "48728:1118"
            exit
            community "service-lpbcks-POC1"
                members "48728:11110"
            exit
            policy-statement "export-to-POC2"
                entry 10
                    from
                        prefix-list "lbl-bgp-lpbck"
                    exit
                    action accept
                        community add "service-lpbcks-IS{data["isis-a-area"]}"
                        origin igp
                    exit
                exit
                default-action drop
                exit
            exit
            policy-statement "import-from-POC2"
                entry 10
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS1"
                    exit
                    action accept
                    exit
                exit
                entry 20
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-POC1"
                    exit
                    action accept
                    exit
                exit
                entry 30
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS2"
                    exit
                    action accept
                    exit
                exit
                entry 40
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS3"
                    exit
                    action accept
                    exit
                exit
                entry 50
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS4"
                    exit
                    action accept
                    exit
                exit
                entry 60
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS5"
                    exit
                    action accept
                    exit
                exit
                entry 70
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS6"
                    exit
                    action accept
                    exit
                exit
                entry 80
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS7"
                    exit
                    action accept
                    exit
                exit
                entry 90
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS8"
                    exit
                    action accept
                    exit
                exit
                entry 100
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS0"
                    exit
                    action accept
                    exit
                exit
                default-action drop
                exit
            exit
            commit
        exit
#--------------------------------------------------
echo "BGP Configuration"
#--------------------------------------------------
        bgp
            min-route-advertisement 5
            outbound-route-filtering
                extended-community
                    send-orf
                exit
            exit
            enable-peer-tracking
            rapid-withdrawal
            next-hop-resolution
                labeled-routes
                    transport-tunnel
                        family vpn
                            resolution-filter
                                ldp
                                rsvp
                                bgp
                            exit
                            resolution filter
                        exit
                        family label-ipv4
                            resolution-filter
                                ldp
                                rsvp
                            exit
                            resolution filter
                        exit
                    exit
                exit
            exit
            group "POC2-lbgp-ipv4"
                family ipv4
                import "import-from-POC2"
                export "export-to-POC2"
                peer-as 48728
                neighbor {data["POC2-1"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
                neighbor {data["POC2-2"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
            exit
            group "Seamless_l3vpns_mp_ibgp"
                family vpn-ipv4
                peer-as 48728
                local-address  {data["loopback"]}
                neighbor {data["POC3-1"]}
                exit
                neighbor {data["POC3-2"]}
                exit
            exit
            no shutdown
        exit
    exit

#--------------------------------------------------
echo "Log all events for service vprn, log syslog tls-client-profile Configuration"
#--------------------------------------------------
    log
    exit
#--------------------------------------------------
echo "System Time NTP Configuration"
#--------------------------------------------------
    system
        time
            ntp
                server 10.100.20.68 prefer
                server 10.200.20.68
                server 172.16.240.41
            exit
        exit
    exit
#--------------------------------------------------
echo "System Configuration Mode Configuration"
#--------------------------------------------------
    system
        management-interface
            configuration-mode classic
        exit
    exit

exit all
"""
    return(txt)
	
def make_route_base_IXR_small (data):
    txt=f"""
exit all
configure
#--------------------------------------------------
echo "System Configuration"
#--------------------------------------------------
    system
        name {data["hostname"]}
        management-interface
            cli
                md-cli
                    no auto-config-save
                exit
            exit
            yang-modules
                no nokia-combined-modules
                nokia-submodules
            exit
        exit
        netconf
            shutdown
            no auto-config-save
        exit
        snmp
            streaming
                no shutdown
            exit
            packet-size 9216
        exit
        time
            ntp
                no authentication-check
                no shutdown
            exit
            sntp
                shutdown
            exit
            zone MSK
        exit
        thresholds
            rmon
                alarm 10 variable-oid sgiCpuUsage.0 interval 5 rising-event 10 rising-threshold 80
                event 10 description "CPU utilization is over 80%"
            exit
        exit
    exit
#--------------------------------------------------
echo "System Security Configuration"
#--------------------------------------------------
   system
        security
            telnet-server
            ftp-server
            profile "SOC"
                default-action deny-all
                entry 8
                    match "configure router interface"
                    action permit
                exit
                entry 9
                    description "Router reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 20
                    match "configure router bgp"
                    action permit
                exit
                entry 70
                    match "admin display-config"
                    action permit
                exit
                entry 80
                    match "show"
                    action permit
                exit
                entry 90
                    match "monitor"
                    action permit
                exit
                entry 100
                    match "telnet"
                    action permit
                exit
                entry 110
                    match "ssh"
                    action permit
                exit
                entry 120
                    match "oam"
                    action permit
                exit
                entry 140
                    match "configure router policy-options"
                    action permit
                exit
                entry 150
                    match "configure port"
                    action permit
                exit
                entry 160
                    match "info"
                    action permit
                exit
                entry 170
                    match "ping"
                    action permit
                exit
                entry 180
                    match "traceroute"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "configure service"
                    action permit
                exit
                entry 220
                    match "exit"
                    action permit
                exit
                entry 230
                    match "admin save"
                    action permit
                exit
                entry 240
                    match "pwc"
                    action permit
                exit
                entry 250
                    match "back"
                    action permit
                exit
                entry 260
                    match "clear"
                    action permit
                exit
                entry 270
                    match "configure lag"
                    action permit
                exit
                entry 280
                    match "configure qos"
                    action permit
                exit
                entry 290
                    match "environment"
                    action deny
                exit
            exit
            profile "TPM"
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "exit"
                    action permit
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 41
                    match "tools dump"
                    action permit
                exit
                entry 42
                    match "sleep"
                    action permit
                exit
                entry 43
                    match "file dir"
                    action permit
                exit
                entry 44
                    match "environment more"
                    action permit
                exit
                entry 50
                    match "password"
                    action permit
                exit
                entry 53
                    match "admin display-config"
                    action permit
                exit
                entry 55
                    match "configure"
                    action deny
                exit
                entry 60
                    match "show config"
                    action deny
                exit
                entry 65
                    match "show li"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action permit
                exit
            exit
            profile "show"
                default-action deny-all
                entry 1
                    match "show"
                    action permit
                exit
                entry 2
                    match "admin display-config"
                    action permit
                exit
                entry 7
                    match "monitor"
                    action permit
                exit
                entry 8
                    match "ping"
                    action permit
                exit
                entry 9
                    match "telnet"
                    action permit
                exit
            exit
            profile "ARCH2"
                default-action deny-all
                entry 1
                    match "oam"
                    action permit
                exit
                entry 2
                    match "ping"
                    action permit
                exit
                entry 3
                    match "admin display-config"
                    action permit
                exit
                entry 4
                    match "configure port"
                    action permit
                exit
                entry 5
                    match "telnet"
                    action permit
                exit
                entry 6
                    match "back"
                    action permit
                exit
                entry 7
                    match "show"
                    action permit
                exit
                entry 8
                    match "ssh"
                    action deny
                exit
                entry 9
                    match "traceroute"
                    action permit
                exit
                entry 10
                    match "monitor"
                    action permit
                exit
                entry 11
                    match "admin save"
                    action permit
                exit
                entry 12
                    match "configure service vprn"
                    action permit
                exit
                entry 13
                    match "environment more "
                    action permit
                exit
                entry 14
                    match "info"
                    action permit
                exit
            exit
            profile "VF-NSU"
                entry 6
                    match "monitor"
                    action permit
                exit
                entry 10
                    match "exec"
                    action deny
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 50
                    match "password"
                    action deny
                exit
                entry 60
                    match "admin display-config"
                    action permit
                exit
                entry 65
                    match "admin"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action deny
                exit
                entry 100
                    match "configure"
                    action deny
                exit
                entry 110
                    match "tools"
                    action deny
                exit
                entry 120
                    match "ping"
                    action permit
                exit
                entry 130
                    match "telnet"
                    action permit
                exit
                entry 140
                    match "traceroute"
                    action permit
                exit
                entry 150
                    match "exit"
                    action permit
                exit
            exit
            profile "tier-1"
                default-action deny-all
                entry 10
                    match "admin tech-support"
                    action permit
                exit
                entry 20
                    match "show"
                    action permit
                exit
                entry 30
                    match "exit"
                    action permit
                exit
            exit
            profile "Operator"
                default-action permit-all
                entry 10
                    match "configure system security"
                    action deny
                exit
                entry 20
                    match "configure li"
                    action deny
                exit
                entry 30
                    match "show li"
                    action deny
                exit
                entry 50
                    match "configure filter"
                    action deny
                exit
            exit
            profile "password"
            exit
            profile "Monitoring"
                default-action deny-all
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "help"
                    action permit
                exit
                entry 30
                    match "logout"
                    action permit
                exit
                entry 40
                    match "password"
                    action permit
                exit
                entry 50
                    match "show"
                    action permit
                exit
                entry 60
                    match "enable-admin"
                    action permit
                exit
                entry 70
                    match "configure"
                    action deny
                exit
                entry 80
                    match "admin display-config"
                    action permit
                exit
                entry 90
                    match "show config"
                    action deny
                exit
                entry 110
                    match "traceroute"
                    action permit
                exit
                entry 120
                    match "exit"
                    action permit
                exit
                entry 130
                    match "configure li"
                    action deny
                exit
                entry 140
                    match "ping"
                    action permit
                exit
                entry 150
                    match "telnet"
                    action permit
                exit
                entry 160
                    match "monitor port"
                    action permit
                exit
                entry 170
                    match "monitor lag"
                    action permit
                exit
                entry 180
                    match "admin save"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "file"
                    action permit
                exit
                entry 211
                    match "ssh"
                    action permit
                exit
                entry 212
                    match "oam lsp-trace"
                    action permit
                exit
                entry 213
                    match "clear port"
                    action permit
                exit
            exit
            profile "NokiaProject"
                default-action permit-all
                entry 1
                    description "reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 2
                    description "securty"
                    match "configure system security"
                    action deny
                exit
            exit
            password
                authentication-order local tacplus radius
                complexity-rules
                    required lowercase 1 uppercase 1 numeric 1 special-character 1
                exit
            exit
            user "AdminSAM5620"
                password "$2y$10$QGGVBkdQhc.V9ceWwfl6..ynxeadOnjPSgFRiAXwGQa3pLGZsN7PK"
                access console ftp snmp 
                console
                    member "default"
                    member "administrative"
                exit
                snmp
                    authentication none
                exit
            exit
            user "admin"
                password "$2y$10$lnMYTNLh3YK1G5e6bCzlg.hcCfnMQdu9HShe6CNxbUW3Li6Eazq4K"
                access console ftp 
                console
                    member "administrative"
                exit
            exit
            user "ameers"
                password "$2y$10$NMjfPL4Kauf1seZOSPcKc./9vc3JrMdoSF0HJlh8GS.kAmTCJHeVO"
                access console ftp snmp 
                console
                    member "default"
                    member "NokiaProject"
                exit
            exit
            user "chrisnanda.ent"
                password "$2y$10$/YtllkeV45TIzAFlkw0Ks.ZOxXjkhrbELh.ZSgivB0oan4lQMheje"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "gnocipfo"
                password "$2y$10$R7ZyDzV9J57tOW/Z3AX9..y0t/PdvBNWEo26.VcWDy77haJOjJHi6"
                access console ftp snmp 
                console
                    member "default"
                    member "show"
                exit
                snmp
                    authentication none
                exit
            exit
            user "samcli"
                password "$2y$10$N5URo5oH0xQ7HBdxK1ms2.kgWEGE5xp0c96vhCEQ.bltHKykRIJe6"
                access console 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "snmpv3user"
                password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
                access snmp 
                snmp
                    authentication hmac-sha1-96 344277c1f4fd287c29f2783ee03567513a99575a privacy cbc-des 344277c1f4fd287c29f2783ee0356751
                    group "nmsPriv"
                exit
            exit
            user "muhammad.ehsan"
                password "$2y$10$Sja5NHyihHEh1hvbMhHdo.ftFhjP1l7cXXMtVOB.dmlyP4EHcRscC"
                access console ftp
                console
                    member "Operator"
                    member "administrative"
                exit
            exit
            user "rohitb"
                password "$2y$10$eyQrBfoT8Gi4XEd1EJexM.EHxOeBBzMlfBf/gVNZ3Ui2DqlocvXjS"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "anas.hammami"
                password "$2y$10$4UStCMbBpydY2jsaEcj9o./b49aloC0qZo7kgdgOXnRXz2jDFsKeW"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "vfq.mali"
                password "$2y$10$zhkSzfGw6ET8iTy7ZDxeA.4vlfqyNbfnl942oWLydTWFGHJ6t2enu"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "deni.sartika"
                password "$2y$10$GPYPa.WMxyxF7TW79K09g.Y0FrP.C7HtIAPVGl8EltTGdPKDn/pi."
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "amogh.acharya"
                password "$2y$10$l2fFGhaiiVE8f0E5mYe62.L5RYheC6Xn1r6UcmiiOMqw5MskjRjqa"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "gems.bo"
                password "$2y$10$tc0o3pEKR3en89sgtk2b2.KC9rwkw5L6pKvfF95n6787vowCmwUzm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.arajeeb"
                password "$2y$10$.ITViSWCVNkgClQNo9TMY.3zg.gBQZCLjjNRY1WhIy.GkN8eC/6dy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            snmp
                access group "nmsPriv" security-model usm security-level privacy read "iso" write "iso" notify "iso"
                access group "nmsPriv" security-model usm security-level privacy context "vprn" prefix read "vprn-view" write "vprn-view" notify "iso"
            exit
        exit
    exit
#--------------------------------------------------
echo "System Login Control Configuration"
#--------------------------------------------------
    system
        login-control
            telnet
                inbound-max-sessions 10
                outbound-max-sessions 10
            exit
            idle-timeout 180
        exit
    exit
#--------------------------------------------------
echo "Log Configuration"
#--------------------------------------------------
    log
        file-id 9 name "9"
            location cf3:
            rollover 2880 retention 500
        exit
        file-id 27 name "27"
            description "SAP drop collection"
            location cf3:
            rollover 15 retention 4
        exit
        file-id 38 name "38"
            description "MBH"
            location cf3:
            rollover 15 retention 4
        exit
        file-id 95 name "95"
            description "Main Log File"
            location cf3:
            rollover 360 retention 72
        exit
        accounting-policy 27
            description "MBH drop statistic collection"
            record service-egress-packets
            collection-interval 15
            to file 27
            no shutdown
        exit
        accounting-policy 28
            description "MBH Drop collection"
            record service-ingress-packets
            collection-interval 15
            to file 38
            no shutdown
        exit
        event-control "system" 2103 generate
        event-control "system" 2104 generate
        event-control "vrtr" 2034 generate
        snmp-trap-group 98 name "98"
            description "5620sam"
            trap-target "10.100.16.132:162" address 10.100.16.132 snmpv2c notify-community "citrix"
            trap-target "10.100.20.68:162" address 10.100.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "10.200.20.68:162" address 10.200.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "D89D672883B8:main1" address 10.200.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
            trap-target "D89D672883B8:main2" address 10.100.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
        exit
        log-id 9 name "9"
            time-format local
            from change
            to file 9
            no shutdown
        exit
        log-id 14 name "14"
            from debug-trace
            to memory
            no shutdown
        exit
        log-id 20 name "20"
            from debug-trace
            no shutdown
        exit
        log-id 95 name "95"
            from main
            to file 95
            no shutdown
        exit
        log-id 98 name "98"
            from main security change
            to snmp 1024
            no shutdown
        exit
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        queue-mgmt-policy "QM_104_12500" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q1" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q2" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q3" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 9380
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q4" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 9380
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q5" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 10
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q6" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 10
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q7" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 2500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q8" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 2500
        exit
        port-qos-policy "NQ_VFQ_IXR_PORT_QOS" create
            description "IXR Network QoS"
            queue "1" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
            exit
            queue "2" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
            exit
            queue "3" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
                scheduler-mode wfq
                    percent-rate 100.00 cir 80.00
                exit
            exit
            queue "4" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
                scheduler-mode wfq
                    percent-rate 100.00 cir 80.00
                exit
            exit
            queue "5" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
                scheduler-mode wfq
                    percent-rate 10.00 cir 10.00
                exit
            exit
            queue "6" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
                scheduler-mode wfq
                    percent-rate 100.00 cir 100.00
                exit
            exit
            queue "7" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
                scheduler-mode wfq
                    percent-rate 100.00 cir 10.00
                exit
            exit
            queue "8" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
                scheduler-mode wfq
                    percent-rate 100.00 cir 20.00
                exit
            exit
        exit
        vlan-qos-policy "102" create
            description "Egress for 2G full IP"
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "103" create
            description "User Traffic delivered to full IP nodeB"
            queue "3" create
                percent-rate 100.00 cir 100.00
            exit
            queue "4" create
                percent-rate 100.00 cir 100.00
            exit
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
                queue-type expedite-hi
                exit
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "104" create
            description "4G LTE SAP Egress policy"
            queue "1" create
                queue-mgmt "QM_104_12500"
            exit
            queue "2" create
                queue-mgmt "QM_104_12500"
            exit
            queue "3" create
                queue-mgmt "QM_104_12500"
            exit
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
            exit
            queue "7" create
                percent-rate 100.00 cir 100.00
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" create
            description "IXR Network QoS"
            queue "1" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
            exit
            queue "2" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
            exit
            queue "3" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
                percent-rate 100.00 cir 80.00
            exit
            queue "4" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
                percent-rate 100.00 cir 80.00
            exit
            queue "5" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
                percent-rate 10.00 cir 10.00
            exit
            queue "6" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
                percent-rate 100.00 cir 100.00
            exit
            queue "7" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
                percent-rate 100.00 cir 10.00
            exit
            queue "8" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
                percent-rate 100.00 cir 20.00
            exit
        exit
        egress-remark-policy "102" create
            description "User Traffic delivered to full IP BTS"
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 6 out-profile 6
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 1 out-profile 1
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
            exit
        exit
        egress-remark-policy "103" create
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 6 out-profile 6
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 5 out-profile 5
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 0 out-profile 0
            exit
        exit
        egress-remark-policy "104" create
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 5 out-profile 5
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
            exit
        exit
        egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" create
            fc af create
                dot1p in-profile 2 out-profile 2
                lsp-exp in-profile 3 out-profile 3
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 5 out-profile 5
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
                lsp-exp in-profile 2 out-profile 2
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
                lsp-exp in-profile 1 out-profile 1
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
                lsp-exp in-profile 4 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 1 out-profile 1
                lsp-exp in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
                lsp-exp in-profile 6 out-profile 6
            exit
        exit
        ingress-classification-policy "100" create
            description "Standard QOS"
            default-action fc "l2"
        exit
        ingress-classification-policy "102" create
            dot1p 1 fc "l2" profile out
            dot1p 3 fc "l1" profile out
            dot1p 4 fc "h2"
            dot1p 6 fc "ef"
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "af11" fc "l2" profile out
            dscp "af31" fc "l1" profile out
            dscp "af41" fc "h2"
        exit
        ingress-classification-policy "103" create
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "nc2" fc "nc"
            dscp "af11" fc "l2" profile out
            dscp "af21" fc "l1" profile out
            dscp "af31" fc "l1" profile out
            dscp "af32" fc "l1"
            dscp "af33" fc "l1"
            dscp "af41" fc "h2"
        exit
        ingress-classification-policy "104" create
            dot1p 0 fc "l2" profile out
            dot1p 3 fc "l1" profile out
            dot1p 4 fc "h2" profile out
            dot1p 5 fc "ef" profile out
            dot1p 6 fc "h1" profile out
            dot1p 7 fc "nc" profile out
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "nc2" fc "h1"
            dscp "af11" fc "l2" profile out
            dscp "af21" fc "l2" profile out
            dscp "af22" fc "l1" profile out
            dscp "af31" fc "l1" profile out
            dscp "af41" fc "l1" profile out
            dscp "af42" fc "h2"
        exit
        ingress-classification-policy "110" create
            description "Real Time VBR QOS"
            default-action fc "h2" profile in
        exit
        ingress-classification-policy "120" create
            description "Signalling QOS"
            default-action fc "h1" profile in
        exit
        ingress-classification-policy "130" create
            description "Critical Data OP QOS"
            default-action fc "af"
        exit
        ingress-classification-policy "140" create
            description "Critical Data IP QOS"
            default-action fc "l1" profile in
        exit
        ingress-classification-policy "150" create
            description "Real Time CBR QOS"
            default-action fc "ef" profile in
        exit
        ingress-classification-policy "160" create
            description "Network Control QOS"
            default-action fc "nc" profile in
        exit
        ingress-classification-policy "NQ_VFQ_IXR_Ing_class" create
            description "NQ_VFQ_IXR_INGRESS"
            default-action fc "l2"
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "cs2" fc "h1"
            dscp "cs3" fc "l1"
            dscp "cs5" fc "h2"
            dscp "nc1" fc "nc"
            dscp "af11" fc "l1"
            dscp "af12" fc "l1"
            dscp "af13" fc "l1"
            dscp "af21" fc "l1"
            dscp "af22" fc "l1"
            dscp "af23" fc "l1"
            dscp "af31" fc "l1"
            dscp "af32" fc "l1"
            dscp "af33" fc "l1"
            dscp "af41" fc "h1"
            dscp "af42" fc "l1"
            lsp-exp 0 fc "l2" profile out
            lsp-exp 1 fc "h2"
            lsp-exp 2 fc "h1"
            lsp-exp 3 fc "af" profile out
            lsp-exp 4 fc "l1"
            lsp-exp 5 fc "ef"
            lsp-exp 6 fc "nc"
        exit
        network-ingress "NQ_VFQ_IXR_Net_Ing" create
            ingress-classification-policy "NQ_VFQ_IXR_Ing_class"
            policer 1
                stat-mode offered-profile-with-discards
            exit
            policer 2
                stat-mode offered-profile-with-discards
            exit
            policer 3
                stat-mode offered-profile-with-discards
            exit
            policer 4
                stat-mode offered-profile-with-discards
            exit
            policer 5
                stat-mode offered-profile-with-discards
            exit
            policer 6
                stat-mode offered-profile-with-discards
            exit
            policer 7
                stat-mode offered-profile-with-discards
            exit
            policer 8
                stat-mode offered-profile-with-discards
            exit
            fc af
                policer 3
            exit
            fc be
                policer 1
            exit
            fc ef
                policer 6
            exit
            fc h1
                policer 7
            exit
            fc h2
                policer 5
            exit
            fc l1
                policer 4
            exit
            fc l2
                policer 2
            exit
            fc nc
                policer 8
            exit
        exit
    exit
#--------------------------------------------------
echo "Oper-Groups (Declarations) Configuration"
#--------------------------------------------------
    service
    exit
#--------------------------------------------------
echo "Card Configuration"
#--------------------------------------------------
    card 1
        card-type imm14-10g-sfp++4-1g-tx
        mda 1
            sync-e
            no shutdown
        exit
        no shutdown
    exit
#--------------------------------------------------
echo "Port Configuration"
#--------------------------------------------------
    port {data["port-a1"]}
        description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
        ethernet
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    port {data["port-b1"]}
        description "NET_{data["hostname"]}:{data["port-b1"]}:NET_{data["far-end-b"]}:{data["port-b2"]}:{data["port-b-type"]}:10GE"
        ethernet
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    port A/1
    exit
#--------------------------------------------------
echo "System Sync-If-Timing Configuration"
#--------------------------------------------------
    system
        sync-if-timing
            begin
            ql-selection
            ref1
                source-port {data["port-a1"]}
                no shutdown
            exit
            revert
            commit
        exit
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        sap-ingress 102 name "102" create
            description "Ingress for 2G full IP"
            ingress-classification-policy "102"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
                rate max cir 100
            exit
            policer 4 create
                rate max cir 100
            exit
            policer 5 create
                rate max cir max
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 103 name "103" create
            ingress-classification-policy "103"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
                rate max cir 100
            exit
            policer 4 create
                rate max cir 100
            exit
            policer 5 create
                rate max cir max
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 104 name "104" create
            description "4G LTE SAP Ingress policy"
            ingress-classification-policy "104"
            policer 1 create
                stat-mode offered-profile-with-discards
                mbs 12500 kilobytes
                cbs 6250 kilobytes
            exit
            policer 2 create
                stat-mode offered-profile-with-discards
                mbs 12500 kilobytes
                cbs 6250 kilobytes
            exit
            policer 3 create
                stat-mode offered-profile-with-discards
            exit
            policer 4 create
                stat-mode offered-profile-with-discards
            exit
            policer 5 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 6 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 7 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 8 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 110 name "110" create
            description "Real Time VBR QOS"
            ingress-classification-policy "110"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 120 name "120" create
            description "Signalling QOS"
            ingress-classification-policy "120"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
                rate max cir max
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 130 name "130" create
            description "Critical Data OP QOS"
            ingress-classification-policy "130"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 140 name "140" create
            description "Critical Data IP QOS"
            ingress-classification-policy "140"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 150 name "150" create
            description "Real Time CBR QOS"
            ingress-classification-policy "150"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 160 name "160" create
            description "Network Control QOS"
            ingress-classification-policy "160"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
    exit
#--------------------------------------------------
echo "Management Router Configuration"
#--------------------------------------------------
    router management
    exit

#--------------------------------------------------
echo "Router (Network Side) Configuration"
#--------------------------------------------------
    router Base
        interface "NET_{data["far-end-a"]}_{data["network-a"]}"
            address {data["network-a"]}/31
            egress
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            port {data["port-a1"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
            exit
            no shutdown
        exit
        interface "NET_{data["far-end-b"]}_{data["network-b"]}"
            address {data["network-b"]}/31
            egress
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            port {data["port-a1"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
            exit
            no shutdown
        exit
        interface "lbl-bgp-lpbck"
            address {data["loopback"]}/32
            loopback
            ingress
            exit
            no shutdown
        exit
        interface "system"
            address {data["system"]}/32
            no shutdown
        exit
        autonomous-system 48728
        ecmp 4
#--------------------------------------------------
echo "Static Route Configuration"
#--------------------------------------------------
        static-route-entry 10.100.20.10/31
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
        static-route-entry 10.100.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
        static-route-entry 10.200.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                wide-metrics-only
            exit
            level 2
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            interface "NET_{data["far-end-b"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            all-l1isis 01:80:c2:00:01:00
            all-l2isis 01:80:c2:00:01:11
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                external-preference 163
                preference 25
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            interface "NET_{data["far-end-b"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "LDP Configuration"
#--------------------------------------------------
        ldp
            import-pmsi-routes
            exit
            tcp-session-parameters
            exit
            interface-parameters
                interface "NET_{data["far-end-a"]}_{data["network-a"]}"  dual-stack
                    ipv4
                        no shutdown
                    exit
                    no shutdown
                exit
                interface "NET_{data["far-end-b"]}_{data["network-b"]}"  dual-stack
                    ipv4
                        no shutdown
                    exit
                    no shutdown
                exit
            exit
            targeted-session
            exit
            no shutdown
        exit
    exit

#--------------------------------------------------
echo "Service Configuration"
#--------------------------------------------------
    service
        vprn 17804 customer 1 create
            description "eNB IPsec Public eUTRAN VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17804{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:178040
            no shutdown
        exit
        vprn 17812 customer 1 create
            description "BTS_BSC_Abis_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17812{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17812
            no shutdown
        exit
        vprn 17813 customer 1 create
            description "eNB_RNC_IuB_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17813{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17813
            no shutdown
        exit
        vprn 17815 customer 1 create
            description "Huawei OAM VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17815{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17815
            no shutdown
        exit
        vprn 55000 name "ENT-4G-5G_Public" customer 1 create
            description "ENT 4G-5G Public Service"
            autonomous-system 48728
            route-distinguisher 48728:55000{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:65100:55000
            no shutdown
        exit
    exit
#--------------------------------------------------
echo "Router (Service Side) Configuration"
#--------------------------------------------------
    router Base
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            no shutdown
        exit
#--------------------------------------------------
echo "Policy Configuration"
#--------------------------------------------------
        policy-options
            begin
            prefix-list "lbl-bgp-lpbck"
                prefix {data["loopback"]}/32 exact
            exit
            prefix-list "only-lbl-bgp-lpbcks"
                prefix 192.168.64.0/20 prefix-length-range 32-32
            exit
            community "service-lpbcks-IS0"
                members "48728:1110"
            exit
            community "service-lpbcks-IS1"
                members "48728:1111"
            exit
            community "service-lpbcks-IS2"
                members "48728:1112"
            exit
            community "service-lpbcks-IS3"
                members "48728:1113"
            exit
            community "service-lpbcks-IS4"
                members "48728:1114"
            exit
            community "service-lpbcks-IS5"
                members "48728:1115"
            exit
            community "service-lpbcks-IS6"
                members "48728:1116"
            exit
            community "service-lpbcks-IS7"
                members "48728:1117"
            exit
            community "service-lpbcks-IS8"
                members "48728:1118"
            exit
            community "service-lpbcks-POC1"
                members "48728:11110"
            exit
            policy-statement "export-to-POC2"
                entry 10
                    from
                        prefix-list "lbl-bgp-lpbck"
                    exit
                    action accept
                        community add "service-lpbcks-IS{data["isis-a-area"]}"
                        origin igp
                    exit
                exit
                default-action drop
                exit
            exit
            policy-statement "import-from-POC2"
                entry 10
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS1"
                    exit
                    action accept
                    exit
                exit
                entry 20
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-POC1"
                    exit
                    action accept
                    exit
                exit
                entry 30
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS2"
                    exit
                    action accept
                    exit
                exit
                entry 40
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS3"
                    exit
                    action accept
                    exit
                exit
                entry 50
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS4"
                    exit
                    action accept
                    exit
                exit
                entry 60
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS5"
                    exit
                    action accept
                    exit
                exit
                entry 70
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS6"
                    exit
                    action accept
                    exit
                exit
                entry 80
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS7"
                    exit
                    action accept
                    exit
                exit
                entry 90
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS8"
                    exit
                    action accept
                    exit
                exit
                entry 100
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS0"
                    exit
                    action accept
                    exit
                exit
                default-action drop
                exit
            exit
            commit
        exit
#--------------------------------------------------
echo "BGP Configuration"
#--------------------------------------------------
        bgp
            min-route-advertisement 5
            outbound-route-filtering
                extended-community
                    send-orf
                exit
            exit
            enable-peer-tracking
            rapid-withdrawal
            next-hop-resolution
                labeled-routes
                    transport-tunnel
                        family vpn
                            resolution-filter
                                ldp
                                rsvp
                                bgp
                            exit
                            resolution filter
                        exit
                        family label-ipv4
                            resolution-filter
                                ldp
                                rsvp
                            exit
                            resolution filter
                        exit
                    exit
                exit
            exit
            group "POC2-lbgp-ipv4"
                family ipv4
                import "import-from-POC2"
                export "export-to-POC2"
                peer-as 48728
                neighbor {data["POC2-1"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
                neighbor {data["POC2-2"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
            exit
            group "Seamless_l3vpns_mp_ibgp"
                family vpn-ipv4
                peer-as 48728
                local-address  {data["loopback"]}
                neighbor {data["POC3-1"]}
                exit
                neighbor {data["POC3-2"]}
                exit
            exit
            no shutdown
        exit
    exit

#--------------------------------------------------
echo "Log all events for service vprn, log syslog tls-client-profile Configuration"
#--------------------------------------------------
    log
    exit
#--------------------------------------------------
echo "System Time NTP Configuration"
#--------------------------------------------------
    system
        time
            ntp
                server 10.100.20.68 prefer
                server 10.200.20.68
                server 172.16.240.41
            exit
        exit
    exit
#--------------------------------------------------
echo "System Configuration Mode Configuration"
#--------------------------------------------------
    system
        management-interface
            configuration-mode classic
        exit
    exit

exit all
"""
    return(txt)
def make_route_base_IXR_big (data):
    txt=f"""
exit all
configure
#--------------------------------------------------
echo "System Configuration"
#--------------------------------------------------
    system
        name {data["hostname"]}
        management-interface
            cli
                md-cli
                    no auto-config-save
                exit
            exit
            yang-modules
                no nokia-combined-modules
                nokia-submodules
            exit
        exit
        netconf
            shutdown
            no auto-config-save
        exit
        snmp
            streaming
                no shutdown
            exit
            packet-size 9216
        exit
        time
            ntp
                no authentication-check
                no shutdown
            exit
            sntp
                shutdown
            exit
            zone MSK
        exit
        thresholds
            rmon
                alarm 10 variable-oid sgiCpuUsage.0 interval 5 rising-event 10 rising-threshold 80
                event 10 description "CPU utilization is over 80%"
            exit
        exit
    exit
#--------------------------------------------------
echo "System Security Configuration"
#--------------------------------------------------
   system
        security
            telnet-server
            ftp-server
            profile "SOC"
                default-action deny-all
                entry 8
                    match "configure router interface"
                    action permit
                exit
                entry 9
                    description "Router reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 20
                    match "configure router bgp"
                    action permit
                exit
                entry 70
                    match "admin display-config"
                    action permit
                exit
                entry 80
                    match "show"
                    action permit
                exit
                entry 90
                    match "monitor"
                    action permit
                exit
                entry 100
                    match "telnet"
                    action permit
                exit
                entry 110
                    match "ssh"
                    action permit
                exit
                entry 120
                    match "oam"
                    action permit
                exit
                entry 140
                    match "configure router policy-options"
                    action permit
                exit
                entry 150
                    match "configure port"
                    action permit
                exit
                entry 160
                    match "info"
                    action permit
                exit
                entry 170
                    match "ping"
                    action permit
                exit
                entry 180
                    match "traceroute"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "configure service"
                    action permit
                exit
                entry 220
                    match "exit"
                    action permit
                exit
                entry 230
                    match "admin save"
                    action permit
                exit
                entry 240
                    match "pwc"
                    action permit
                exit
                entry 250
                    match "back"
                    action permit
                exit
                entry 260
                    match "clear"
                    action permit
                exit
                entry 270
                    match "configure lag"
                    action permit
                exit
                entry 280
                    match "configure qos"
                    action permit
                exit
                entry 290
                    match "environment"
                    action deny
                exit
            exit
            profile "TPM"
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "exit"
                    action permit
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 41
                    match "tools dump"
                    action permit
                exit
                entry 42
                    match "sleep"
                    action permit
                exit
                entry 43
                    match "file dir"
                    action permit
                exit
                entry 44
                    match "environment more"
                    action permit
                exit
                entry 50
                    match "password"
                    action permit
                exit
                entry 53
                    match "admin display-config"
                    action permit
                exit
                entry 55
                    match "configure"
                    action deny
                exit
                entry 60
                    match "show config"
                    action deny
                exit
                entry 65
                    match "show li"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action permit
                exit
            exit
            profile "show"
                default-action deny-all
                entry 1
                    match "show"
                    action permit
                exit
                entry 2
                    match "admin display-config"
                    action permit
                exit
                entry 7
                    match "monitor"
                    action permit
                exit
                entry 8
                    match "ping"
                    action permit
                exit
                entry 9
                    match "telnet"
                    action permit
                exit
            exit
            profile "ARCH2"
                default-action deny-all
                entry 1
                    match "oam"
                    action permit
                exit
                entry 2
                    match "ping"
                    action permit
                exit
                entry 3
                    match "admin display-config"
                    action permit
                exit
                entry 4
                    match "configure port"
                    action permit
                exit
                entry 5
                    match "telnet"
                    action permit
                exit
                entry 6
                    match "back"
                    action permit
                exit
                entry 7
                    match "show"
                    action permit
                exit
                entry 8
                    match "ssh"
                    action deny
                exit
                entry 9
                    match "traceroute"
                    action permit
                exit
                entry 10
                    match "monitor"
                    action permit
                exit
                entry 11
                    match "admin save"
                    action permit
                exit
                entry 12
                    match "configure service vprn"
                    action permit
                exit
                entry 13
                    match "environment more "
                    action permit
                exit
                entry 14
                    match "info"
                    action permit
                exit
            exit
            profile "VF-NSU"
                entry 6
                    match "monitor"
                    action permit
                exit
                entry 10
                    match "exec"
                    action deny
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 50
                    match "password"
                    action deny
                exit
                entry 60
                    match "admin display-config"
                    action permit
                exit
                entry 65
                    match "admin"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action deny
                exit
                entry 100
                    match "configure"
                    action deny
                exit
                entry 110
                    match "tools"
                    action deny
                exit
                entry 120
                    match "ping"
                    action permit
                exit
                entry 130
                    match "telnet"
                    action permit
                exit
                entry 140
                    match "traceroute"
                    action permit
                exit
                entry 150
                    match "exit"
                    action permit
                exit
            exit
            profile "tier-1"
                default-action deny-all
                entry 10
                    match "admin tech-support"
                    action permit
                exit
                entry 20
                    match "show"
                    action permit
                exit
                entry 30
                    match "exit"
                    action permit
                exit
            exit
            profile "Operator"
                default-action permit-all
                entry 10
                    match "configure system security"
                    action deny
                exit
                entry 20
                    match "configure li"
                    action deny
                exit
                entry 30
                    match "show li"
                    action deny
                exit
                entry 50
                    match "configure filter"
                    action deny
                exit
            exit
            profile "password"
            exit
            profile "Monitoring"
                default-action deny-all
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "help"
                    action permit
                exit
                entry 30
                    match "logout"
                    action permit
                exit
                entry 40
                    match "password"
                    action permit
                exit
                entry 50
                    match "show"
                    action permit
                exit
                entry 60
                    match "enable-admin"
                    action permit
                exit
                entry 70
                    match "configure"
                    action deny
                exit
                entry 80
                    match "admin display-config"
                    action permit
                exit
                entry 90
                    match "show config"
                    action deny
                exit
                entry 110
                    match "traceroute"
                    action permit
                exit
                entry 120
                    match "exit"
                    action permit
                exit
                entry 130
                    match "configure li"
                    action deny
                exit
                entry 140
                    match "ping"
                    action permit
                exit
                entry 150
                    match "telnet"
                    action permit
                exit
                entry 160
                    match "monitor port"
                    action permit
                exit
                entry 170
                    match "monitor lag"
                    action permit
                exit
                entry 180
                    match "admin save"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "file"
                    action permit
                exit
                entry 211
                    match "ssh"
                    action permit
                exit
                entry 212
                    match "oam lsp-trace"
                    action permit
                exit
                entry 213
                    match "clear port"
                    action permit
                exit
            exit
            profile "NokiaProject"
                default-action permit-all
                entry 1
                    description "reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 2
                    description "securty"
                    match "configure system security"
                    action deny
                exit
            exit
            password
                authentication-order local tacplus radius
                complexity-rules
                    required lowercase 1 uppercase 1 numeric 1 special-character 1
                exit
            exit
            user "AdminSAM5620"
                password "$2y$10$QGGVBkdQhc.V9ceWwfl6..ynxeadOnjPSgFRiAXwGQa3pLGZsN7PK"
                access console ftp snmp 
                console
                    member "default"
                    member "administrative"
                exit
                snmp
                    authentication none
                exit
            exit
            user "admin"
                password "$2y$10$lnMYTNLh3YK1G5e6bCzlg.hcCfnMQdu9HShe6CNxbUW3Li6Eazq4K"
                access console ftp 
                console
                    member "administrative"
                exit
            exit
            user "ameers"
                password "$2y$10$NMjfPL4Kauf1seZOSPcKc./9vc3JrMdoSF0HJlh8GS.kAmTCJHeVO"
                access console ftp snmp 
                console
                    member "default"
                    member "NokiaProject"
                exit
            exit
            user "chrisnanda.ent"
                password "$2y$10$/YtllkeV45TIzAFlkw0Ks.ZOxXjkhrbELh.ZSgivB0oan4lQMheje"
                access console ftp
                console
                    member "default"
                    member "administrative"
					exit
            exit
            user "gnocipfo"
                password "$2y$10$R7ZyDzV9J57tOW/Z3AX9..y0t/PdvBNWEo26.VcWDy77haJOjJHi6"
                access console ftp snmp 
                console
                    member "default"
                    member "show"
                exit
                snmp
                    authentication none
                exit
            exit
            user "samcli"
                password "$2y$10$N5URo5oH0xQ7HBdxK1ms2.kgWEGE5xp0c96vhCEQ.bltHKykRIJe6"
                access console 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "snmpv3user"
                password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
                access snmp 
                snmp
                    authentication hmac-sha1-96 344277c1f4fd287c29f2783ee03567513a99575a privacy cbc-des 344277c1f4fd287c29f2783ee0356751
                    group "nmsPriv"
                exit
            exit
            user "muhammad.ehsan"
                password "$2y$10$Sja5NHyihHEh1hvbMhHdo.ftFhjP1l7cXXMtVOB.dmlyP4EHcRscC"
                access console ftp
                console
                    member "Operator"
                    member "administrative"
                exit
            exit
            user "rohitb"
                password "$2y$10$eyQrBfoT8Gi4XEd1EJexM.EHxOeBBzMlfBf/gVNZ3Ui2DqlocvXjS"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "anas.hammami"
                password "$2y$10$4UStCMbBpydY2jsaEcj9o./b49aloC0qZo7kgdgOXnRXz2jDFsKeW"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "vfq.mali"
                password "$2y$10$zhkSzfGw6ET8iTy7ZDxeA.4vlfqyNbfnl942oWLydTWFGHJ6t2enu"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "deni.sartika"
                password "$2y$10$GPYPa.WMxyxF7TW79K09g.Y0FrP.C7HtIAPVGl8EltTGdPKDn/pi."
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "amogh.acharya"
                password "$2y$10$l2fFGhaiiVE8f0E5mYe62.L5RYheC6Xn1r6UcmiiOMqw5MskjRjqa"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "gems.bo"
                password "$2y$10$tc0o3pEKR3en89sgtk2b2.KC9rwkw5L6pKvfF95n6787vowCmwUzm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.arajeeb"
                password "$2y$10$.ITViSWCVNkgClQNo9TMY.3zg.gBQZCLjjNRY1WhIy.GkN8eC/6dy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            snmp
                access group "nmsPriv" security-model usm security-level privacy read "iso" write "iso" notify "iso"
                access group "nmsPriv" security-model usm security-level privacy context "vprn" prefix read "vprn-view" write "vprn-view" notify "iso"
            exit
        exit
    exit
#--------------------------------------------------
echo "System Login Control Configuration"
#--------------------------------------------------
    system
        login-control
            telnet
                inbound-max-sessions 10
                outbound-max-sessions 10
            exit
            idle-timeout 180
        exit
    exit
#--------------------------------------------------
echo "Log Configuration"
#--------------------------------------------------
    log
        file-id 9 name "9"
            location cf3:
            rollover 2880 retention 500
        exit
        file-id 27 name "27"
            description "SAP drop collection"
            location cf3:
            rollover 15 retention 4
        exit
        file-id 38 name "38"
            description "MBH"
            location cf3:
            rollover 15 retention 4
        exit
        file-id 95 name "95"
            description "Main Log File"
            location cf3:
            rollover 360 retention 72
        exit
        accounting-policy 27
            description "MBH drop statistic collection"
            record service-egress-packets
            collection-interval 15
            to file 27
            no shutdown
        exit
        accounting-policy 28
            description "MBH Drop collection"
            record service-ingress-packets
            collection-interval 15
            to file 38
            no shutdown
        exit
        event-control "system" 2103 generate
        event-control "system" 2104 generate
        event-control "vrtr" 2034 generate
        snmp-trap-group 98 name "98"
            description "5620sam"
            trap-target "10.100.16.132:162" address 10.100.16.132 snmpv2c notify-community "citrix"
            trap-target "10.100.20.68:162" address 10.100.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "10.200.20.68:162" address 10.200.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "D89D672883B8:main1" address 10.200.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
            trap-target "D89D672883B8:main2" address 10.100.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
        exit
        log-id 9 name "9"
            time-format local
            from change
            to file 9
            no shutdown
        exit
        log-id 14 name "14"
            from debug-trace
            to memory
            no shutdown
        exit
        log-id 20 name "20"
            from debug-trace
            no shutdown
        exit
        log-id 95 name "95"
            from main
            to file 95
            no shutdown
        exit
        log-id 98 name "98"
            from main security change
            to snmp 1024
            no shutdown
        exit
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        queue-mgmt-policy "QM_104_12500" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q1" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q2" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 12500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q3" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 9380
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q4" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 9380
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q5" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 10
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q6" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 10
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q7" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 2500
        exit
        queue-mgmt-policy "NQ_VFQ_IXR_QMP_Q8" create
            high-slope
                shutdown
            exit
            low-slope
                shutdown
            exit
            exceed-slope
                shutdown
            exit
            highplus-slope
                shutdown
            exit
            mbs 2500
        exit
        port-qos-policy "NQ_VFQ_IXR_PORT_QOS" create
            description "IXR Network QoS"
            queue "1" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
            exit
            queue "2" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
            exit
            queue "3" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
                scheduler-mode wfq
                    percent-rate 100.00 cir 80.00
                exit
            exit
            queue "4" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
                scheduler-mode wfq
                    percent-rate 100.00 cir 80.00
                exit
            exit
            queue "5" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
                scheduler-mode wfq
                    percent-rate 10.00 cir 10.00
                exit
            exit
            queue "6" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
                scheduler-mode wfq
                    percent-rate 100.00 cir 100.00
                exit
            exit
            queue "7" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
                scheduler-mode wfq
                    percent-rate 100.00 cir 10.00
                exit
            exit
            queue "8" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
                scheduler-mode wfq
                    percent-rate 100.00 cir 20.00
                exit
            exit
        exit
        vlan-qos-policy "102" create
            description "Egress for 2G full IP"
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "103" create
            description "User Traffic delivered to full IP nodeB"
            queue "3" create
                percent-rate 100.00 cir 100.00
            exit
            queue "4" create
                percent-rate 100.00 cir 100.00
            exit
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
                queue-type expedite-hi
                exit
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "104" create
            description "4G LTE SAP Egress policy"
            queue "1" create
                queue-mgmt "QM_104_12500"
            exit
            queue "2" create
                queue-mgmt "QM_104_12500"
            exit
            queue "3" create
                queue-mgmt "QM_104_12500"
            exit
            queue "5" create
                percent-rate 100.00 cir 100.00
            exit
            queue "6" create
                percent-rate 100.00 cir 100.00
            exit
            queue "7" create
                percent-rate 100.00 cir 100.00
            exit
            queue "8" create
                percent-rate 100.00 cir 100.00
            exit
        exit
        vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS" create
            description "IXR Network QoS"
            queue "1" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q1"
            exit
            queue "2" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q2"
            exit
            queue "3" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q3"
                percent-rate 100.00 cir 80.00
            exit
            queue "4" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q4"
                percent-rate 100.00 cir 80.00
            exit
            queue "5" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q5"
                percent-rate 10.00 cir 10.00
            exit
            queue "6" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q6"
                percent-rate 100.00 cir 100.00
            exit
            queue "7" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q7"
                percent-rate 100.00 cir 10.00
            exit
            queue "8" create
                queue-mgmt "NQ_VFQ_IXR_QMP_Q8"
                percent-rate 100.00 cir 20.00
            exit
        exit
        egress-remark-policy "102" create
            description "User Traffic delivered to full IP BTS"
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 6 out-profile 6
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 1 out-profile 1
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
            exit
        exit
        egress-remark-policy "103" create
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 6 out-profile 6
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 5 out-profile 5
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 0 out-profile 0
            exit
        exit
        egress-remark-policy "104" create
            fc af create
                dot1p in-profile 2 out-profile 2
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 5 out-profile 5
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
            exit
        exit
        egress-remark-policy "NQ_VFQ_IXR_Eg_Remark" create
            fc af create
                dot1p in-profile 2 out-profile 2
                lsp-exp in-profile 3 out-profile 3
            exit
            fc be create
                dot1p in-profile 0 out-profile 0
            exit
            fc ef create
                dot1p in-profile 5 out-profile 5
            exit
            fc h1 create
                dot1p in-profile 6 out-profile 6
                lsp-exp in-profile 2 out-profile 2
            exit
            fc h2 create
                dot1p in-profile 4 out-profile 4
                lsp-exp in-profile 1 out-profile 1
            exit
            fc l1 create
                dot1p in-profile 3 out-profile 3
                lsp-exp in-profile 4 out-profile 3
            exit
            fc l2 create
                dot1p in-profile 1 out-profile 1
                lsp-exp in-profile 0 out-profile 0
            exit
            fc nc create
                dot1p in-profile 7 out-profile 7
                lsp-exp in-profile 6 out-profile 6
            exit
        exit
        ingress-classification-policy "100" create
            description "Standard QOS"
            default-action fc "l2"
        exit
        ingress-classification-policy "102" create
            dot1p 1 fc "l2" profile out
            dot1p 3 fc "l1" profile out
            dot1p 4 fc "h2"
            dot1p 6 fc "ef"
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "af11" fc "l2" profile out
            dscp "af31" fc "l1" profile out
            dscp "af41" fc "h2"
        exit
        ingress-classification-policy "103" create
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "nc2" fc "nc"
            dscp "af11" fc "l2" profile out
            dscp "af21" fc "l1" profile out
            dscp "af31" fc "l1" profile out
            dscp "af32" fc "l1"
            dscp "af33" fc "l1"
            dscp "af41" fc "h2"
        exit
        ingress-classification-policy "104" create
            dot1p 0 fc "l2" profile out
            dot1p 3 fc "l1" profile out
            dot1p 4 fc "h2" profile out
            dot1p 5 fc "ef" profile out
            dot1p 6 fc "h1" profile out
            dot1p 7 fc "nc" profile out
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "nc2" fc "h1"
            dscp "af11" fc "l2" profile out
            dscp "af21" fc "l2" profile out
            dscp "af22" fc "l1" profile out
            dscp "af31" fc "l1" profile out
            dscp "af41" fc "l1" profile out
            dscp "af42" fc "h2"
        exit
        ingress-classification-policy "110" create
            description "Real Time VBR QOS"
            default-action fc "h2" profile in
        exit
        ingress-classification-policy "120" create
            description "Signalling QOS"
            default-action fc "h1" profile in
        exit
        ingress-classification-policy "130" create
            description "Critical Data OP QOS"
            default-action fc "af"
        exit
        ingress-classification-policy "140" create
            description "Critical Data IP QOS"
            default-action fc "l1" profile in
        exit
        ingress-classification-policy "150" create
            description "Real Time CBR QOS"
            default-action fc "ef" profile in
        exit
        ingress-classification-policy "160" create
            description "Network Control QOS"
            default-action fc "nc" profile in
        exit
        ingress-classification-policy "NQ_VFQ_IXR_Ing_class" create
            description "NQ_VFQ_IXR_INGRESS"
            default-action fc "l2"
            dscp "be" fc "l2" profile out
            dscp "ef" fc "ef"
            dscp "cs2" fc "h1"
            dscp "cs3" fc "l1"
            dscp "cs5" fc "h2"
            dscp "nc1" fc "nc"
            dscp "af11" fc "l1"
            dscp "af12" fc "l1"
            dscp "af13" fc "l1"
            dscp "af21" fc "l1"
            dscp "af22" fc "l1"
            dscp "af23" fc "l1"
            dscp "af31" fc "l1"
            dscp "af32" fc "l1"
            dscp "af33" fc "l1"
            dscp "af41" fc "h1"
            dscp "af42" fc "l1"
            lsp-exp 0 fc "l2" profile out
            lsp-exp 1 fc "h2"
            lsp-exp 2 fc "h1"
            lsp-exp 3 fc "af" profile out
            lsp-exp 4 fc "l1"
            lsp-exp 5 fc "ef"
            lsp-exp 6 fc "nc"
        exit
        network-ingress "NQ_VFQ_IXR_Net_Ing" create
            ingress-classification-policy "NQ_VFQ_IXR_Ing_class"
            policer 1
                stat-mode offered-profile-with-discards
            exit
            policer 2
                stat-mode offered-profile-with-discards
            exit
            policer 3
                stat-mode offered-profile-with-discards
            exit
            policer 4
                stat-mode offered-profile-with-discards
            exit
            policer 5
                stat-mode offered-profile-with-discards
            exit
            policer 6
                stat-mode offered-profile-with-discards
            exit
            policer 7
                stat-mode offered-profile-with-discards
            exit
            policer 8
                stat-mode offered-profile-with-discards
            exit
            fc af
                policer 3
            exit
            fc be
                policer 1
            exit
            fc ef
                policer 6
            exit
            fc h1
                policer 7
            exit
            fc h2
                policer 5
            exit
            fc l1
                policer 4
            exit
            fc l2
                policer 2
            exit
            fc nc
                policer 8
            exit
        exit
    exit
#--------------------------------------------------
echo "Oper-Groups (Declarations) Configuration"
#--------------------------------------------------
    service
    exit
#--------------------------------------------------
echo "Card Configuration"
#--------------------------------------------------
    card 1
        card-type imm24-sfp++8-sfp28+2-qsfp28
        mda 1
            sync-e
            no shutdown
        exit
        no shutdown
    exit
#--------------------------------------------------
echo "Port Configuration"
#--------------------------------------------------
    port {data["port-a1"]}
        description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
        ethernet
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    port {data["port-b1"]}
        description "NET_{data["hostname"]}:{data["port-b1"]}:NET_{data["far-end-b"]}:{data["port-b2"]}:{data["port-b-type"]}:10GE"
        ethernet
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    port A/1
    exit
#--------------------------------------------------
echo "System Sync-If-Timing Configuration"
#--------------------------------------------------
    system
        sync-if-timing
            begin
            ql-selection
            ref1
                source-port {data["port-a1"]}
                no shutdown
            exit
            revert
            commit
        exit
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        sap-ingress 102 name "102" create
            description "Ingress for 2G full IP"
            ingress-classification-policy "102"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
                rate max cir 100
            exit
            policer 4 create
                rate max cir 100
            exit
            policer 5 create
                rate max cir max
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 103 name "103" create
            ingress-classification-policy "103"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
                rate max cir 100
            exit
            policer 4 create
                rate max cir 100
            exit
            policer 5 create
                rate max cir max
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 104 name "104" create
            description "4G LTE SAP Ingress policy"
            ingress-classification-policy "104"
            policer 1 create
                stat-mode offered-profile-with-discards
                mbs 12500 kilobytes
                cbs 6250 kilobytes
            exit
            policer 2 create
                stat-mode offered-profile-with-discards
                mbs 12500 kilobytes
                cbs 6250 kilobytes
            exit
            policer 3 create
                stat-mode offered-profile-with-discards
            exit
            policer 4 create
                stat-mode offered-profile-with-discards
            exit
            policer 5 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 6 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 7 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            policer 8 create
                stat-mode offered-profile-with-discards
                rate max cir max
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 110 name "110" create
            description "Real Time VBR QOS"
            ingress-classification-policy "110"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 120 name "120" create
            description "Signalling QOS"
            ingress-classification-policy "120"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
                rate max cir max
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 130 name "130" create
            description "Critical Data OP QOS"
            ingress-classification-policy "130"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 140 name "140" create
            description "Critical Data IP QOS"
            ingress-classification-policy "140"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 150 name "150" create
            description "Real Time CBR QOS"
            ingress-classification-policy "150"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
                rate max cir max
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
        sap-ingress 160 name "160" create
            description "Network Control QOS"
            ingress-classification-policy "160"
            policer 1 create
            exit
            policer 2 create
            exit
            policer 3 create
            exit
            policer 4 create
            exit
            policer 5 create
            exit
            policer 6 create
            exit
            policer 7 create
            exit
            policer 8 create
            exit
            fc "af" create
                policer 3
            exit
            fc "be" create
                policer 1
            exit
            fc "ef" create
                policer 6
            exit
            fc "h1" create
                policer 7
            exit
            fc "h2" create
                policer 5
            exit
            fc "l1" create
                policer 4
            exit
            fc "l2" create
                policer 2
            exit
            fc "nc" create
                policer 8
            exit
        exit
    exit
#--------------------------------------------------
echo "Management Router Configuration"
#--------------------------------------------------
    router management
    exit

#--------------------------------------------------
echo "Router (Network Side) Configuration"
#--------------------------------------------------
    router Base
        interface "NET_{data["far-end-a"]}_{data["network-a"]}"
            address {data["network-a"]}/31
            egress
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            port {data["port-a1"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
            exit
            no shutdown
        exit
        interface "NET_{data["far-end-b"]}_{data["network-b"]}"
            address {data["network-b"]}/31
            egress
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            port {data["port-b1"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
            exit
            no shutdown
        exit
        interface "lbl-bgp-lpbck"
            address {data["loopback"]}/32
            loopback
            ingress
            exit
            no shutdown
        exit
        interface "system"
            address {data["system"]}/32
            no shutdown
        exit
        autonomous-system 48728
        ecmp 4
#--------------------------------------------------
echo "Static Route Configuration"
#--------------------------------------------------
        static-route-entry 10.100.20.10/31
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
        static-route-entry 10.100.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
        static-route-entry 10.200.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
            next-hop {increment_last_octet(data["network-b"])}
                no shutdown
            exit
        exit
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                wide-metrics-only
            exit
            level 2
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            interface "NET_{data["far-end-b"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            all-l1isis 01:80:c2:00:01:00
            all-l2isis 01:80:c2:00:01:11
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                external-preference 163
                preference 25
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            interface "NET_{data["far-end-b"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "LDP Configuration"
#--------------------------------------------------
        ldp
            import-pmsi-routes
            exit
            tcp-session-parameters
            exit
            interface-parameters
                interface "NET_{data["far-end-a"]}_{data["network-a"]}"  dual-stack
                    ipv4
                        no shutdown
                    exit
                    no shutdown
                exit
                interface "NET_{data["far-end-b"]}_{data["network-b"]}"  dual-stack
                    ipv4
                        no shutdown
                    exit
                    no shutdown
                exit
            exit
            targeted-session
            exit
            no shutdown
        exit
    exit

#--------------------------------------------------
echo "Service Configuration"
#--------------------------------------------------
    service
        vprn 17804 customer 1 create
            description "eNB IPsec Public eUTRAN VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17804{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:178040
            no shutdown
        exit
        vprn 17812 customer 1 create
            description "BTS_BSC_Abis_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17812{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17812
            no shutdown
        exit
        vprn 17813 customer 1 create
            description "eNB_RNC_IuB_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17813{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17813
            no shutdown
        exit
        vprn 17815 customer 1 create
            description "Huawei OAM VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17815{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17815
            no shutdown
        exit
        vprn 55000 name "ENT-4G-5G_Public" customer 1 create
            description "ENT 4G-5G Public Service"
            autonomous-system 48728
            route-distinguisher 48728:55000{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:65100:55000
            no shutdown
        exit
    exit
#--------------------------------------------------
echo "Router (Service Side) Configuration"
#--------------------------------------------------
    router Base
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            no shutdown
        exit
#--------------------------------------------------
echo "Policy Configuration"
#--------------------------------------------------
        policy-options
            begin
            prefix-list "lbl-bgp-lpbck"
                prefix {data["loopback"]}/32 exact
            exit
            prefix-list "only-lbl-bgp-lpbcks"
                prefix 192.168.64.0/20 prefix-length-range 32-32
            exit
            community "service-lpbcks-IS0"
                members "48728:1110"
            exit
            community "service-lpbcks-IS1"
                members "48728:1111"
            exit
            community "service-lpbcks-IS2"
                members "48728:1112"
            exit
            community "service-lpbcks-IS3"
                members "48728:1113"
            exit
            community "service-lpbcks-IS4"
                members "48728:1114"
            exit
            community "service-lpbcks-IS5"
                members "48728:1115"
            exit
            community "service-lpbcks-IS6"
                members "48728:1116"
            exit
            community "service-lpbcks-IS7"
                members "48728:1117"
            exit
            community "service-lpbcks-IS8"
                members "48728:1118"
            exit
            community "service-lpbcks-POC1"
                members "48728:11110"
            exit
            policy-statement "export-to-POC2"
                entry 10
                    from
                        prefix-list "lbl-bgp-lpbck"
                    exit
                    action accept
                        community add "service-lpbcks-IS{data["isis-a-area"]}"
                        origin igp
                    exit
                exit
                default-action drop
                exit
            exit
            policy-statement "import-from-POC2"
                entry 10
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS1"
                    exit
                    action accept
                    exit
                exit
                entry 20
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-POC1"
                    exit
                    action accept
                    exit
                exit
                entry 30
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS2"
                    exit
                    action accept
                    exit
                exit
                entry 40
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS3"
                    exit
                    action accept
                    exit
                exit
                entry 50
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS4"
                    exit
                    action accept
                    exit
                exit
                entry 60
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS5"
                    exit
                    action accept
                    exit
                exit
                entry 70
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS6"
                    exit
                    action accept
                    exit
                exit
                entry 80
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS7"
                    exit
                    action accept
                    exit
                exit
                entry 90
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS8"
                    exit
                    action accept
                    exit
                exit
                entry 100
                    from
                        protocol bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS0"
                    exit
                    action accept
                    exit
                exit
                default-action drop
                exit
            exit
            commit
        exit
#--------------------------------------------------
echo "BGP Configuration"
#--------------------------------------------------
        bgp
            min-route-advertisement 5
            outbound-route-filtering
                extended-community
                    send-orf
                exit
            exit
            enable-peer-tracking
            rapid-withdrawal
            next-hop-resolution
                labeled-routes
                    transport-tunnel
                        family vpn
                            resolution-filter
                                ldp
                                rsvp
                                bgp
                            exit
                            resolution filter
                        exit
                        family label-ipv4
                            resolution-filter
                                ldp
                                rsvp
                            exit
                            resolution filter
                        exit
                    exit
                exit
            exit
            group "POC2-lbgp-ipv4"
                family ipv4
                import "import-from-POC2"
                export "export-to-POC2"
                peer-as 48728
                neighbor {data["POC2-1"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
                neighbor {data["POC2-2"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
            exit
            group "Seamless_l3vpns_mp_ibgp"
                family vpn-ipv4
                peer-as 48728
                local-address  {data["loopback"]}
                neighbor {data["POC3-1"]}
                exit
                neighbor {data["POC3-2"]}
                exit
            exit
            no shutdown
        exit
    exit

#--------------------------------------------------
echo "Log all events for service vprn, log syslog tls-client-profile Configuration"
#--------------------------------------------------
    log
    exit
#--------------------------------------------------
echo "System Time NTP Configuration"
#--------------------------------------------------
    system
        time
            ntp
                server 10.100.20.68 prefer
                server 10.200.20.68
                server 172.16.240.41
            exit
        exit
    exit
#--------------------------------------------------
echo "System Configuration Mode Configuration"
#--------------------------------------------------
    system
        management-interface
            configuration-mode classic
        exit
    exit

exit all
"""
    return(txt)
def make_route_base (data):
    txt=f"""
exit all
configure
#--------------------------------------------------
echo "System Configuration"
#--------------------------------------------------
    system
        name {data["hostname"]}
        dns
        exit
        snmp
            packet-size 9216
        exit
        time
            ntp
                no authentication-check
                server 10.100.20.68 prefer
                server 10.200.20.68
                server 172.16.240.41
                no shutdown
            exit
            sntp
                shutdown
            exit
            zone MSK 
        exit
        thresholds
            rmon
                alarm 10 variable-oid sgiCpuUsage.0 interval 5 rising-event 10 rising-threshold 80 
                event 10 description "CPU utilization is over 80%" 
            exit
        exit
    exit
#--------------------------------------------------
echo "System Security Configuration"
#--------------------------------------------------
   system
        security
            telnet-server
            ftp-server
            profile "SOC"
                default-action deny-all
                entry 8
                    match "configure router interface"
                    action permit
                exit
                entry 9
                    description "Router reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 20
                    match "configure router bgp"
                    action permit
                exit
                entry 70
                    match "admin display-config"
                    action permit
                exit
                entry 80
                    match "show"
                    action permit
                exit
                entry 90
                    match "monitor"
                    action permit
                exit
                entry 100
                    match "telnet"
                    action permit
                exit
                entry 110
                    match "ssh"
                    action permit
                exit
                entry 120
                    match "oam"
                    action permit
                exit
                entry 140
                    match "configure router policy-options"
                    action permit
                exit
                entry 150
                    match "configure port"
                    action permit
                exit
                entry 160
                    match "info"
                    action permit
                exit
                entry 170
                    match "ping"
                    action permit
                exit
                entry 180
                    match "traceroute"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "configure service"
                    action permit
                exit
                entry 220
                    match "exit"
                    action permit
                exit
                entry 230
                    match "admin save"
                    action permit
                exit
                entry 240
                    match "pwc"
                    action permit
                exit
                entry 250
                    match "back"
                    action permit
                exit
                entry 260
                    match "clear"
                    action permit
                exit
                entry 270
                    match "configure lag"
                    action permit
                exit
                entry 280
                    match "configure qos"
                    action permit
                exit
                entry 290
                    match "environment"
                    action deny
                exit
            exit
            profile "TPM"
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "exit"
                    action permit
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 41
                    match "tools dump"
                    action permit
                exit
                entry 42
                    match "sleep"
                    action permit
                exit
                entry 43
                    match "file dir"
                    action permit
                exit
                entry 44
                    match "environment more"
                    action permit
                exit
                entry 50
                    match "password"
                    action permit
                exit
                entry 53
                    match "admin display-config"
                    action permit
                exit
                entry 55
                    match "configure"
                    action deny
                exit
                entry 60
                    match "show config"
                    action deny
                exit
                entry 65
                    match "show li"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action permit
                exit
            exit
            profile "show"
                default-action deny-all
                entry 1
                    match "show"
                    action permit
                exit
                entry 2
                    match "admin display-config"
                    action permit
                exit
                entry 7
                    match "monitor"
                    action permit
                exit
                entry 8
                    match "ping"
                    action permit
                exit
                entry 9
                    match "telnet"
                    action permit
                exit
            exit
            profile "ARCH2"
                default-action deny-all
                entry 1
                    match "oam"
                    action permit
                exit
                entry 2
                    match "ping"
                    action permit
                exit
                entry 3
                    match "admin display-config"
                    action permit
                exit
                entry 4
                    match "configure port"
                    action permit
                exit
                entry 5
                    match "telnet"
                    action permit
                exit
                entry 6
                    match "back"
                    action permit
                exit
                entry 7
                    match "show"
                    action permit
                exit
                entry 8
                    match "ssh"
                    action deny
                exit
                entry 9
                    match "traceroute"
                    action permit
                exit
                entry 10
                    match "monitor"
                    action permit
                exit
                entry 11
                    match "admin save"
                    action permit
                exit
                entry 12
                    match "configure service vprn"
                    action permit
                exit
                entry 13
                    match "environment more "
                    action permit
                exit
                entry 14
                    match "info"
                    action permit
                exit
            exit
            profile "VF-NSU"
                entry 6
                    match "monitor"
                    action permit
                exit
                entry 10
                    match "exec"
                    action deny
                exit
                entry 30
                    match "help"
                    action permit
                exit
                entry 40
                    match "logout"
                    action permit
                exit
                entry 50
                    match "password"
                    action deny
                exit
                entry 60
                    match "admin display-config"
                    action permit
                exit
                entry 65
                    match "admin"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action deny
                exit
                entry 100
                    match "configure"
                    action deny
                exit
                entry 110
                    match "tools"
                    action deny
                exit
                entry 120
                    match "ping"
                    action permit
                exit
                entry 130
                    match "telnet"
                    action permit
                exit
                entry 140
                    match "traceroute"
                    action permit
                exit
                entry 150
                    match "exit"
                    action permit
                exit
            exit
            profile "tier-1"
                default-action deny-all
                entry 10
                    match "admin tech-support"
                    action permit
                exit
                entry 20
                    match "show"
                    action permit
                exit
                entry 30
                    match "exit"
                    action permit
                exit
            exit
            profile "Operator"
                default-action permit-all
                entry 10
                    match "configure system security"
                    action deny
                exit
                entry 20
                    match "configure li"
                    action deny
                exit
                entry 30
                    match "show li"
                    action deny
                exit
                entry 50
                    match "configure filter"
                    action deny
                exit
            exit
            profile "password"
            exit
            profile "Monitoring"
                default-action deny-all
                entry 10
                    match "exec"
                    action permit
                exit
                entry 20
                    match "help"
                    action permit
                exit
                entry 30
                    match "logout"
                    action permit
                exit
                entry 40
                    match "password"
                    action permit
                exit
                entry 50
                    match "show"
                    action permit
                exit
                entry 60
                    match "enable-admin"
                    action permit
                exit
                entry 70
                    match "configure"
                    action deny
                exit
                entry 80
                    match "admin display-config"
                    action permit
                exit
                entry 90
                    match "show config"
                    action deny
                exit
                entry 110
                    match "traceroute"
                    action permit
                exit
                entry 120
                    match "exit"
                    action permit
                exit
                entry 130
                    match "configure li"
                    action deny
                exit
                entry 140
                    match "ping"
                    action permit
                exit
                entry 150
                    match "telnet"
                    action permit
                exit
                entry 160
                    match "monitor port"
                    action permit
                exit
                entry 170
                    match "monitor lag"
                    action permit
                exit
                entry 180
                    match "admin save"
                    action permit
                exit
                entry 190
                    match "admin tech-support"
                    action permit
                exit
                entry 200
                    match "history"
                    action permit
                exit
                entry 210
                    match "file"
                    action permit
                exit
                entry 211
                    match "ssh"
                    action permit
                exit
                entry 212
                    match "oam lsp-trace"
                    action permit
                exit
                entry 213
                    match "clear port"
                    action permit
                exit
            exit
            profile "NokiaProject"
                default-action permit-all
                entry 1
                    description "reboot"
                    match "admin reboot"
                    action deny
                exit
                entry 2
                    description "securty"
                    match "configure system security"
                    action deny
                exit
            exit
            password
                authentication-order local tacplus radius
                complexity-rules
                    required lowercase 1 uppercase 1 numeric 1 special-character 1
                exit
            exit
            user "AdminSAM5620"
                password "$2y$10$QGGVBkdQhc.V9ceWwfl6..ynxeadOnjPSgFRiAXwGQa3pLGZsN7PK"
                access console ftp snmp 
                console
                    member "default"
                    member "administrative"
                exit
                snmp
                    authentication none
                exit
            exit
            user "admin"
                password "$2y$10$lnMYTNLh3YK1G5e6bCzlg.hcCfnMQdu9HShe6CNxbUW3Li6Eazq4K"
                access console ftp 
                console
                    member "administrative"
                exit
            exit
            user "ameers"
                password "$2y$10$NMjfPL4Kauf1seZOSPcKc./9vc3JrMdoSF0HJlh8GS.kAmTCJHeVO"
                access console ftp snmp 
                console
                    member "default"
                    member "NokiaProject"
                exit
            exit
            user "chrisnanda.ent"
                password "$2y$10$/YtllkeV45TIzAFlkw0Ks.ZOxXjkhrbELh.ZSgivB0oan4lQMheje"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "gnocipfo"
                password "$2y$10$R7ZyDzV9J57tOW/Z3AX9..y0t/PdvBNWEo26.VcWDy77haJOjJHi6"
                access console ftp snmp 
                console
                    member "default"
                    member "show"
                exit
                snmp
                    authentication none
                exit
            exit
            user "samcli"
                password "$2y$10$N5URo5oH0xQ7HBdxK1ms2.kgWEGE5xp0c96vhCEQ.bltHKykRIJe6"
                access console 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "snmpv3user"
                password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
                access snmp 
                snmp
                    authentication hmac-sha1-96 344277c1f4fd287c29f2783ee03567513a99575a privacy cbc-des 344277c1f4fd287c29f2783ee0356751
                    group "nmsPriv"
                exit
            exit
            user "muhammad.ehsan"
                password "$2y$10$Sja5NHyihHEh1hvbMhHdo.ftFhjP1l7cXXMtVOB.dmlyP4EHcRscC"
                access console ftp
                console
                    member "Operator"
                    member "administrative"
                exit
            exit
            user "rohitb"
                password "$2y$10$eyQrBfoT8Gi4XEd1EJexM.EHxOeBBzMlfBf/gVNZ3Ui2DqlocvXjS"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "anas.hammami"
                password "$2y$10$4UStCMbBpydY2jsaEcj9o./b49aloC0qZo7kgdgOXnRXz2jDFsKeW"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "vfq.mali"
                password "$2y$10$zhkSzfGw6ET8iTy7ZDxeA.4vlfqyNbfnl942oWLydTWFGHJ6t2enu"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "deni.sartika"
                password "$2y$10$GPYPa.WMxyxF7TW79K09g.Y0FrP.C7HtIAPVGl8EltTGdPKDn/pi."
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "amogh.acharya"
                password "$2y$10$l2fFGhaiiVE8f0E5mYe62.L5RYheC6Xn1r6UcmiiOMqw5MskjRjqa"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "gems.bo"
                password "$2y$10$tc0o3pEKR3en89sgtk2b2.KC9rwkw5L6pKvfF95n6787vowCmwUzm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.arajeeb"
                password "$2y$10$.ITViSWCVNkgClQNo9TMY.3zg.gBQZCLjjNRY1WhIy.GkN8eC/6dy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            snmp
                access group "nmsPriv" security-model usm security-level privacy read "iso" write "iso" notify "iso"
                access group "nmsPriv" security-model usm security-level privacy context "vprn" prefix read "vprn-view" write "vprn-view" notify "iso"
            exit
        exit
    exit
#--------------------------------------------------
echo "System Login Control Configuration"
#--------------------------------------------------
    system
        login-control
            idle-timeout 180
        exit
    exit
#--------------------------------------------------
echo "Log Configuration"
#--------------------------------------------------
    log 
        file-id 9 
            location cf3: 
            rollover 2880 retention 500 
        exit 
        file-id 27 
            description "SAP drop collection"
            location cf3: 
            rollover 15 retention 4 
        exit 
        file-id 38 
            description "MBH"
            location cf3: 
            rollover 15 retention 4 
        exit 
        accounting-policy 27 
            description "MBH drop statistic collection" 
            record service-egress-packets 
            collection-interval 15 
            to file 27 
            no shutdown 
        exit 
        accounting-policy 28 
            description "MBH Drop collection" 
            record service-ingress-packets 
            collection-interval 15 
            to file 38 
            no shutdown 
        exit 
        event-control "system" 2103 generate
        event-control "system" 2104 generate
        event-control "vrtr" 2034 generate
        snmp-trap-group 98
            description "5620sam"
            trap-target "10.100.16.132:162" address 10.100.16.132 snmpv2c notify-community "citrix"
            trap-target "10.100.20.68:162" address 10.100.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "10.200.20.68:162" address 10.200.20.68 snmpv2c notify-community "privatetrap98"
            trap-target "D89D672883B8:main1" address 10.200.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
            trap-target "D89D672883B8:main2" address 10.100.20.68 snmpv3 notify-community "snmpv3user" security-level privacy
        exit 
        log-id 9
            time-format local
            from change 
            to file 9
            no shutdown
        exit
        log-id 14
            from debug-trace 
            to memory
            no shutdown
        exit
        log-id 20
            from debug-trace 
            no shutdown
        exit
        log-id 98
            from main security 
            to snmp 1024
            no shutdown
        exit
    exit 
#--------------------------------------------------
echo "System Security Cpm Hw Filters and PKI Configuration"
#--------------------------------------------------
    system
        security
        exit
    exit
#--------------------------------------------------
echo "VLAN-Filter Configuration"
#--------------------------------------------------
    filter
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        atm-td-profile 2 create
            description "UBR"
        exit
        atm-td-profile 3 create
            description "rtVBR"
            service-category rt-vbr
            traffic pir 3808 mbs 0 
        exit
        atm-td-profile 4 create
            description "UP DS rtVBR 2E1"
            service-category rt-vbr
            traffic sir 848 pir 3808 
        exit
        atm-td-profile 5 create
            description "UP NDS nrtVBR 2E1"
            service-category nrt-vbr
            traffic sir 1696 pir 3808 mbs 80 
        exit
        atm-td-profile 6 create
            description "RANAP CS rtVBR"
            service-category rt-vbr
            traffic sir 340 pir 848 mbs 40 
        exit
        atm-td-profile 7 create
            description "IU CS CBR"
            service-category cbr
            traffic pir 5088 
        exit
        atm-td-profile 8 create
            description "RANAP PS rtVBR"
            service-category rt-vbr
            traffic sir 679 pir 1696 mbs 40 
        exit
        atm-td-profile 12 create
            description "HSDPA UBR 1E1"
            traffic pir 3808 
        exit
        atm-td-profile 13 create
            description "OAM rtVBR 1E1"
        exit
        atm-td-profile 14 create
            description "UP DS rtVBR 4E1"
            service-category rt-vbr
            traffic sir 3808 pir 3808 mbs 16 
        exit
        atm-td-profile 15 create
            description "UP NDS nrtVBR 4E1"
            service-category nrt-vbr
            traffic sir 848 pir 3808 mbs 40 
        exit
        atm-td-profile 20 create
            description "ATM QoS Policy-20"
        exit
        atm-td-profile 22 create
            description "HSDPA UBR 2E1"
            service-category rt-vbr
            traffic sir 2742 pir 3808 
        exit
        atm-td-profile 23 create
            description "OAM rtVBR 2E1"
        exit
        atm-td-profile 24 create
            description "ATM QoS Policy-24"
            service-category rt-vbr
            traffic sir 3808 pir 3808 
        exit
        atm-td-profile 25 create
            description "ATM QoS Policy-25"
            service-category nrt-vbr
            traffic sir 848 pir 3808 mbs 80 
        exit
        atm-td-profile 32 create
            description "HSDPA UBR 3E1"
            traffic pir 5711 
        exit
        atm-td-profile 33 create
            description "OAM rtVBR 3E1"
        exit
        atm-td-profile 34 create
            description "ATM QoS Policy-34"
            service-category rt-vbr
            traffic sir 5711 pir 5711 mbs 48 
        exit
        atm-td-profile 35 create
            description "ATM QoS Policy-35"
            service-category nrt-vbr
            traffic sir 1272 pir 5711 mbs 120 
        exit
        atm-td-profile 42 create
            description "HSDPA UBR 4E1"
            traffic pir 7615 
        exit
        atm-td-profile 43 create
            description "OAM rtVBR 4E1"
        exit
        atm-td-profile 44 create
            description "ATM QoS Policy-44"
            service-category rt-vbr
            traffic sir 7615 pir 7615 mbs 64 
        exit
        atm-td-profile 45 create
            description "ATM QoS Policy-45"
            service-category nrt-vbr
            traffic sir 1696 pir 7615 mbs 160 
        exit
        atm-td-profile 52 create
            description "HSDPA UBR 5E1"
            traffic pir 9519 
        exit
        atm-td-profile 53 create
            description "OAM rtVBR 5E1"
        exit
        atm-td-profile 54 create
            description "ATM QoS Policy-54"
            service-category rt-vbr
            traffic sir 9519 pir 9519 mbs 80 
        exit
        atm-td-profile 55 create
            description "ATM QoS Policy-55"
            service-category nrt-vbr
            traffic sir 2120 pir 9519 mbs 200 
        exit
        atm-td-profile 62 create
            description "HSDPA UBR 6E1"
            traffic pir 11423 
        exit
        atm-td-profile 63 create
            description "OAM rtVBR 6E1"
        exit
        atm-td-profile 64 create
            description "UP DS rtVBR 6E1"
            service-category rt-vbr
            traffic sir 11423 pir 11423 mbs 96 
        exit
        atm-td-profile 65 create
            description "UP NDS nrtVBR 6E1"
            service-category nrt-vbr
            traffic sir 2544 pir 11423 mbs 240 
        exit
        atm-td-profile 72 create
            description "HSDPA UBR 7xE1s"
        exit
        atm-td-profile 92 create
            description "HSDPA UBR 2E1 test "
            traffic pir 3808 
        exit
        atm-td-profile 93 create
            description "OAM rtVBR 2E1 test"
            service-category rt-vbr
            traffic sir 2742 pir 3808 
        exit
        atm-td-profile 94 create
            description "UP DS rtVBR 2E1 test"
            service-category rt-vbr
            traffic sir 2742 pir 3808 
        exit
        atm-td-profile 95 create
            description "UP NDS nrtVBR 2E1 test"
            service-category nrt-vbr
            traffic sir 3046 pir 3808 mbs 72 
        exit
        atm-td-profile 99 create
            description "test"
            service-category rt-vbr
            traffic sir 424 pir 3808 
        exit
        atm-td-profile 102 create
            description "test OAM"
        exit
        atm-td-profile 114 create
            description "UP DS rtVBR 1E1"
            service-category rt-vbr
            traffic sir 3808 pir 3808 mbs 16 
        exit
        atm-td-profile 115 create
            description "UP NDS nrtVBR 1E1"
            service-category nrt-vbr
            traffic sir 848 pir 3808 mbs 40 
        exit
        atm-td-profile 224 create
            description "UP DS rtVBR 2E1"
            service-category rt-vbr
            traffic sir 3808 pir 3808 
        exit
        atm-td-profile 225 create
            description "UP NDS nrtVBR 2E1"
            service-category nrt-vbr
            traffic sir 848 pir 3808 mbs 80 
        exit
        atm-td-profile 334 create
            service-category rt-vbr
            traffic sir 5711 pir 5711 mbs 48 
        exit
        atm-td-profile 335 create
            service-category nrt-vbr
            traffic sir 1272 pir 5711 mbs 120 
        exit
        atm-td-profile 444 create
            service-category rt-vbr
            traffic sir 7615 pir 7615 mbs 64 
        exit
        atm-td-profile 445 create
            service-category nrt-vbr
            traffic sir 1696 pir 7615 mbs 160 
        exit
        atm-td-profile 554 create
            description "UP DS rtVBR 5E1 TEST "
            service-category rt-vbr
            traffic sir 9519 pir 9519 mbs 80 
        exit
        atm-td-profile 555 create
            description "UP NDS nrtVBR 5E1 TEST"
            service-category nrt-vbr
            traffic sir 2120 pir 9519 mbs 200 
        exit
        atm-td-profile 664 create
            description "UP DS rtVBR 6E1 TEST "
            service-category rt-vbr
            traffic sir 11423 pir 11423 mbs 96 
        exit
        atm-td-profile 665 create
            description "UP NDS nrtVBR 6E1 TEST "
            service-category nrt-vbr
            traffic sir 2544 pir 11423 mbs 240 
        exit
        network-queue "NQ_VFQ_SAR" create
            description "SAR Network QoS"
            queue 1 create
                mbs 12.50
                cbs 0.01
                high-prio-only 10
            exit
            queue 3 create
                rate 100 cir 80
                mbs 9.38
                cbs 1
            exit
            queue 5 create
                rate 10 cir 10
                mbs 0.01
                cbs 0.01
            exit
            queue 6 create
                rate 100 cir 100
                mbs 0.01
                cbs 0.01
            exit
            queue 7 create
                rate 100 cir 10
                mbs 2.50
                cbs 0.25
            exit
            queue 8 create
                rate 100 cir 20
                mbs 2.50
                cbs 0.50
            exit
            queue 9 multipoint create
                mbs 50
                cbs 1
                high-prio-only 10
            exit
            fc af create
                multicast-queue 9
                queue 3
            exit
            fc be create
                multicast-queue 9
                queue 1
            exit
            fc ef create
                multicast-queue 9
                queue 6
            exit
            fc h1 create
                multicast-queue 9
                queue 7
            exit
            fc h2 create
                multicast-queue 9
                queue 5
            exit
            fc l1 create
                multicast-queue 9
                queue 3
            exit
            fc l2 create
                multicast-queue 9
                queue 1
            exit
            fc nc create
                multicast-queue 9
                queue 8
            exit
        exit
    exit
#--------------------------------------------------
echo "QoS Policy Configuration"
#--------------------------------------------------
    qos
        sap-ingress 10 create
            queue 1 create
            exit
            default-fc "ef"
        exit
        sap-ingress 100 create
            description "Standard QOS"
            queue 1 create
            exit
            fc "l2" create
                queue 1
            exit
            default-fc "l2"
            default-priority high
        exit
        sap-ingress 101 create
            description "QOS - 3G OAM received from full IP nodeB"
            queue 1 create
            exit
            fc "l2" create
                queue 1
            exit
            default-fc "l2"
        exit
        sap-ingress 102 create
            description "User Traffic received from full IP BTS"
            queue 1 create
            exit
            queue 2 create
            exit
            queue 3 create
            exit
            queue 5 expedite create
                rate max cir max
            exit
            queue 6 expedite create
                rate max cir max
            exit
            queue 8 expedite create
                rate max cir max
            exit
            fc "ef" create
                queue 6
            exit
            fc "h2" create
                queue 5
            exit
            fc "l1" create
                queue 3
            exit
            fc "l2" create
                queue 2
            exit
            fc "nc" create
                queue 8
            exit
            dscp ef fc "ef" priority high
            dscp af41 fc "h2" priority high
            dscp af21 af31 fc "l1"
            dscp be af11 fc "l2"
            dscp nc2 fc "nc" priority high
        exit
        sap-ingress 103 create
            description "User Traffic received from full IP nodeB"
            queue 1 create
            exit
            queue 2 create
            exit
            queue 3 create
                rate max cir 100
            exit
            queue 5 expedite create
                rate max cir max
            exit
            queue 6 expedite create
                rate max cir max
            exit
            queue 8 expedite create
                rate max cir max
            exit
            fc "ef" create
                queue 6
            exit
            fc "h2" create
                queue 5
            exit
            fc "l1" create
                queue 3
            exit
            fc "l2" create
                queue 2
            exit
            fc "nc" create
                queue 8
            exit
            dscp ef fc "ef" priority high
            dscp af41 fc "h2" priority high
            dscp af32 af33 fc "l1" priority high
            dscp af21 af31 fc "l1"
            dscp be af11 fc "l2"
            dscp nc2 fc "nc" priority high
        exit
        sap-ingress 104 create
            description "User Traffic received from 4G eNodeB"
            queue 1 create
                mbs 12500 kilobytes
                cbs 6250
            exit
            queue 2 create
                mbs 12500 kilobytes
                cbs 6250
            exit
            queue 3 create
            exit
            queue 5 expedite create
                rate max cir max
            exit
            queue 6 expedite create
                rate max cir max
            exit
            queue 7 expedite create
                rate max cir max
            exit
            queue 8 expedite create
                rate max cir max
            exit
            fc "ef" create
                queue 6
            exit
            fc "h1" create
                queue 7
            exit
            fc "h2" create
                queue 5
            exit
            fc "l1" create
                queue 3
            exit
            fc "l2" create
                queue 2
            exit
            fc "nc" create
                queue 8
            exit
            dot1p 7 fc "nc"
            dscp ef fc "ef" priority high
            dscp nc2 fc "h1"
            dscp af42 fc "h2" priority high
            dscp af41 fc "h2"
            dscp af21 af22 af31 fc "l1"
            dscp be af11 af13 fc "l2"
        exit
        sap-ingress 110 create
            description "Real Time VBR QOS"
            queue 1 create
            exit
            fc "h2" create
                queue 1
            exit
            default-fc "h2"
            default-priority high
        exit
        sap-ingress 120 create
            description "Signalling QOS"
            queue 1 create
            exit
            fc "h1" create
                queue 1
            exit
            default-fc "h1"
            default-priority high
        exit
        sap-ingress 130 create
            description "Critical Data OP QOS"
            queue 1 create
            exit
            fc "af" create
                queue 1
            exit
            default-fc "af"
        exit
        sap-ingress 140 create
            description "Critical Data IP QOS"
            queue 1 create
            exit
            fc "l1" create
                queue 1
            exit
            default-fc "l1"
        exit
        sap-ingress 150 create
            description "Real Time CBR QOS"
            queue 1 create
                rate max cir 4096
            exit
            fc "ef" create
                queue 1
            exit
            default-fc "ef"
            default-priority high
        exit
        sap-ingress 160 create
            description "Network Control QOS"
            queue 1 create
            exit
            fc "nc" create
                queue 1
            exit
            default-fc "nc"
            default-priority high
        exit
        sap-egress 101 create
            description "QoS - 3G OAM egressing to full IP nodeB"
            queue 1 create
            exit
            fc l2 create
                queue 1
                dot1p 0
                dscp be
            exit 
        exit
        sap-egress 102 create
            description "User Traffic delivered to full IP BTS"
            queue 1 create
            exit
            queue 2 create
            exit
            queue 3 create
            exit
            queue 5 expedite create
                rate max cir max
            exit
            queue 6 expedite create
                rate max cir max
            exit
            queue 8 expedite create
                rate max cir max
            exit
            fc ef create
                queue 6
                dot1p 5
            exit 
            fc h2 create
                queue 5
                dot1p 4
            exit 
            fc l1 create
                queue 3
                dot1p 2
            exit 
            fc l2 create
                queue 2
                dot1p 0
            exit 
            fc nc create
                queue 8
                dot1p 6
            exit 
        exit
        sap-egress 103 create
            description "User Traffic delivered to full IP nodeB"
            queue 1 create
            exit
            queue 2 create
            exit
            queue 3 create
                rate max cir 100
            exit
            queue 5 expedite create
                rate max cir max
            exit
            queue 6 expedite create
                rate max cir max
            exit
            queue 8 expedite create
                rate max cir max
            exit
            fc ef create
                queue 6
                dot1p 5
            exit 
            fc h2 create
                queue 5
                dot1p 4
            exit 
            fc l1 create
                queue 3
                dot1p 3
            exit 
            fc l2 create
                queue 2
                dot1p 1
            exit 
            fc nc create
                queue 8
                dot1p 6
            exit 
        exit
        sap-egress 104 create
            description "User Traffic delivered 4G eNodeB"
            queue 1 create
                cbs 6250
                mbs 12500 kilobytes
            exit
            queue 2 create
                cbs 6250
                mbs 12500 kilobytes
            exit
            queue 3 create
            exit
            queue 5 expedite create
                rate max cir max
            exit
            queue 6 expedite create
                rate max cir max
            exit
            queue 8 expedite create
                rate max cir max
            exit
            fc ef create
                queue 6
                dot1p 5
            exit 
            fc h2 create
                queue 5
                dot1p 4
            exit 
            fc l1 create
                queue 3
                dot1p 2
            exit 
            fc l2 create
                queue 2
                dot1p 1
            exit 
            fc nc create
                queue 8
                dot1p 6
            exit 
        exit
        mc-mlppp
        exit
        network 10 create
            ingress
                default-action fc l2 profile out
                dscp be fc l2 profile out
                dscp ef fc ef profile in
                dscp cs2 fc h1 profile in
                dscp cs3 fc l1 profile in
                dscp cs5 fc h2 profile in
                dscp nc1 fc nc profile in
                dscp af11 fc l1 profile in
                dscp af12 fc l1 profile in
                dscp af13 fc l1 profile in
                dscp af21 fc l1 profile in
                dscp af22 fc l1 profile in
                dscp af23 fc l1 profile in
                dscp af31 fc l1 profile in
                dscp af32 fc l1 profile in
                dscp af33 fc l1 profile in
                dscp af41 fc h1 profile in
                dscp af42 fc l1 profile in
                lsp-exp 0 fc l2 profile out
                lsp-exp 1 fc h2 profile in
                lsp-exp 2 fc h1 profile in
                lsp-exp 3 fc af profile out
                lsp-exp 4 fc l1 profile in
                lsp-exp 5 fc ef profile in
                lsp-exp 6 fc nc profile in
            exit
            egress
                fc af
                    lsp-exp-out-profile 3
                exit
                fc h1
                    lsp-exp-in-profile 2
                    lsp-exp-out-profile 2
                exit
                fc h2
                    lsp-exp-in-profile 1
                    lsp-exp-out-profile 1
                exit
                fc l1
                    lsp-exp-in-profile 4
                    lsp-exp-out-profile 3
                exit
                fc l2
                    lsp-exp-in-profile 0
                    lsp-exp-out-profile 0
                    dot1p-in-profile 0
                    dot1p-out-profile 0
                exit
                fc nc
                    lsp-exp-in-profile 6
                    lsp-exp-out-profile 6
                exit
            exit
        exit
    exit
#--------------------------------------------------
echo "Card Configuration"
#--------------------------------------------------
    card 1
        card-type iom-sar
        mda 1
            mda-type i8-chds1-x
            network
                ingress
                    queue-policy "NQ_VFQ_SAR"
                exit
            exit
            no shutdown
        exit
        mda 2
            mda-type i7-mix-eth
            network
                ingress
                    queue-policy "NQ_VFQ_SAR"
                exit
            exit
            no shutdown
        exit
        mda 3
            mda-type i7-mix-eth
            network
                ingress
                    queue-policy "NQ_VFQ_SAR"
                exit
            exit
            no shutdown
        exit
        no shutdown
    exit
#--------------------------------------------------
echo "Port Configuration"
#--------------------------------------------------
    port 1/2/3
        description "Site_{data["Site"]}_Huawei_SRAN"
        ethernet
            encap-type dot1q
            mtu 1818
            ssm
                no shutdown
            exit
        exit
        no shutdown
    exit
    port {data["port-a1"]}
        description "NET_{data["hostname"]}:{data["port-a1"]}:NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:10GE"
        ethernet
            mode network
            mtu 2102
            network
                queue-policy "NQ_VFQ_SAR"
            exit
            ssm
                no shutdown
            exit
        exit
        no shutdown
    exit
    port {data["port-b1"]}
        description "NET_{data["hostname"]}:{data["port-b1"]}:NET_{data["far-end-b"]}:{data["port-b2"]}:{data["port-b-type"]}:10GE"
        ethernet
            mode network
            mtu 2102
            network
                queue-policy "NQ_VFQ_SAR"
            exit
            ssm
                no shutdown
            exit
        exit
        no shutdown
    exit
#--------------------------------------------------
echo "External Alarm Configuration"
#--------------------------------------------------
    external-alarms
    exit
#--------------------------------------------------
echo "Network Security Configuration"
#--------------------------------------------------
    security
        logging
        exit
        begin
        commit
    exit
#--------------------------------------------------
echo "Management Router Configuration"
#--------------------------------------------------
    router management
    exit

#--------------------------------------------------
echo "Router (Network Side) Configuration"
#--------------------------------------------------
    router Base
        interface "NET_{data["far-end-a"]}_{data["network-a"]}"
            address {data["network-a"]}/31
            port 1/2/7
            qos 10
            no shutdown
        exit
        interface "lbl-bgp-lpbck"
            address {data["loopback"]}/32
            loopback
            no shutdown
        exit
        interface "system"
            address {data["system"]}/32
            no shutdown
        exit
        autonomous-system 48728
        ecmp 4
#--------------------------------------------------
echo "Static Route Configuration"
#--------------------------------------------------
        static-route-entry 10.100.20.10/31
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
        exit
        static-route-entry 10.100.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
        exit
        static-route-entry 10.200.20.64/28
            next-hop {increment_last_octet(data["network-a"])}
                no shutdown
            exit
        exit
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                wide-metrics-only
            exit
            level 2
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            area-id 49.0974
            authentication-key ALU
            authentication-type message-digest
            lsp-lifetime 65535
            traffic-engineering
            iid-tlv-enable
            timers
                lsp-wait 8000 lsp-initial-wait 10 lsp-second-wait 1000
                spf-wait 2000 spf-initial-wait 50 spf-second-wait 100
            exit
            level 1
                external-preference 163
                preference 25
                wide-metrics-only
            exit
            interface "system"
                no shutdown
            exit
            interface "NET_{data["far-end-a"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
                no shutdown
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "LDP Configuration"
#--------------------------------------------------
        ldp
            interface-parameters
                interface "NET_{data["far-end-a"]}_{data["network-a"]}" dual-stack
                    ipv4
                        no shutdown
                    exit
                    no shutdown
                exit
            exit
            targeted-session
            exit
            no shutdown
        exit
    exit

#--------------------------------------------------
echo "Service Configuration"
#--------------------------------------------------
    service
        customer 1 create
            description "Default customer"
        exit
        vprn 17804 customer 1 create
            description "eNB IPsec Public eUTRAN VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17804{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:178040
            no shutdown
        exit
        vprn 17812 customer 1 create
            description "BTS_BSC_Abis_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17812{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17812
            no shutdown
        exit
        vprn 17813 customer 1 create
            description "eNB_RNC_IuB_VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17813{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17813
            no shutdown
        exit
        vprn 17815 customer 1 create
            description "Huawei OAM VPRN"
            autonomous-system 48728
            route-distinguisher 48728:17815{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    ldp
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:48728:17815
            no shutdown
        exit
        vprn 55000 name "ENT-4G-5G_Public" customer 1 create
            description "ENT 4G-5G Public Service"
            autonomous-system 48728
            route-distinguisher 48728:55000{data["Site"]}
            auto-bind-tunnel
                resolution-filter
                    rsvp
                exit
                resolution filter
            exit
            vrf-target target:65100:55000
            no shutdown
        exit
    exit
#--------------------------------------------------
echo "Router (Service Side) Configuration"
#--------------------------------------------------
    router Base
#--------------------------------------------------
echo "ISIS Configuration"
#--------------------------------------------------
        isis 0
            no shutdown
        exit
#--------------------------------------------------
echo "ISIS (Inst: {data["isis-a-area"]}) Configuration"
#--------------------------------------------------
        isis {data["isis-a-area"]}
            no shutdown
        exit
#--------------------------------------------------
echo "Policy Configuration"
#--------------------------------------------------
        policy-options
            begin
            prefix-list "lbl-bgp-lpbck"
                prefix {data["loopback"]}/32 exact
            exit
            prefix-list "only-lbl-bgp-lpbcks"
                prefix 192.168.64.0/20 prefix-length-range 32-32
            exit
            community "service-lpbcks-IS0" members "48728:1110"
            community "service-lpbcks-IS1" members "48728:1111"
            community "service-lpbcks-IS2" members "48728:1112"
            community "service-lpbcks-IS3" members "48728:1113"
            community "service-lpbcks-IS4" members "48728:1114"
            community "service-lpbcks-IS5" members "48728:1115"
            community "service-lpbcks-IS6" members "48728:1116"
            community "service-lpbcks-IS7" members "48728:1117"
            community "service-lpbcks-IS8" members "48728:1118"
            community "service-lpbcks-POC1" members "48728:11110"
            policy-statement "export-to-POC2"
                entry 10
                    from
                        prefix-list "lbl-bgp-lpbck"
                    exit
                    action accept
                        community add "service-lpbcks-IS{data["isis-a-area"]}"
                        origin igp
                    exit
                exit
                default-action reject
            exit
            policy-statement "import-from-POC2"
                entry 10
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS2"
                    exit
                    action accept
                    exit
                exit
                entry 20
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-POC1"
                    exit
                    action accept
                    exit
                exit
                entry 30
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS1"
                    exit
                    action accept
                    exit
                exit
                entry 40
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS3"
                    exit
                    action accept
                    exit
                exit
                entry 50
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS4"
                    exit
                    action accept
                    exit
                exit
                entry 60
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS5"
                    exit
                    action accept
                    exit
                exit
                entry 70
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS6"
                    exit
                    action accept
                    exit
                exit
                entry 80
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS7"
                    exit
                    action accept
                    exit
                exit
                entry 90
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS8"
                    exit
                    action accept
                    exit
                exit
                entry 100
                    from
                        protocol bgp bgp-label
                        prefix-list "only-lbl-bgp-lpbcks"
                        community "service-lpbcks-IS0"
                    exit
                    action accept
                    exit
                exit
                default-action reject
            exit
            commit
        exit
#--------------------------------------------------
echo "BGP Configuration"
#--------------------------------------------------
        bgp
            min-route-advertisement 5
            outbound-route-filtering
                extended-community
                    send-orf
                exit
            exit
            enable-peer-tracking
            rapid-withdrawal
            backup-path ipv4 label-ipv4
            next-hop-resolution
                label-route-transport-tunnel
                    family vpn
                        resolution-filter
                            ldp
                            rsvp
                        exit
                        resolution filter
                    exit
                    family label-ipv4
                        resolution-filter
                            ldp
                            rsvp
                        exit
                        resolution filter
                    exit
                exit
            exit
            group "POC2-lbgp-ipv4"
                family ipv4
                import "import-from-POC2" 
                export "export-to-POC2" 
                peer-as 48728
                neighbor {data["POC2-1"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
                neighbor {data["POC2-2"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
            exit
            group "Seamless_l3vpns_mp_ibgp"
                family vpn-ipv4
                peer-as 48728
                local-address  {data["loopback"]}
                neighbor {data["POC3-1"]}
                exit
                neighbor {data["POC3-2"]}
                exit
            exit
            no shutdown
        exit
#--------------------------------------------------
echo "Network Security Zone Configuration"
#--------------------------------------------------
    exit

#--------------------------------------------------
echo "System Sync-If-Timing Configuration"
#--------------------------------------------------
    system
        sync-if-timing
            begin
            ql-selection
            ref-order ref1 ref2 external 
            ref1
                source-port {data["port-a1"]}
                no shutdown
            exit
            revert
            commit
        exit
    exit
#--------------------------------------------------
echo "System Time Configuration"
#--------------------------------------------------
    system
        time
            ntp
            exit
        exit
    exit

exit all
bof persist on
configure system snmp no shutdown
admin save cf3:/{data["hostname"]}.cfg
bof primary-config cf3:/{data["hostname"]}.cfg
bof save"""
    return (txt)
def make_farend1(data):
    txt=f"""
configure
    port {data["port-a2"]}
        description "NET_{data["far-end-a"]}:{data["port-a2"]}:{data["port-a-type"]}:{data["hostname"]}:{data["port-a1"]}::10GE"
        ethernet
            mode network
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            hold-time up 5
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    router Base
        interface "NET_{data["hostname"]}_{data["network-a"]}"
            address {increment_last_octet(data["network-a"])}/31
            port {data["port-a2"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            no shutdown
        exit
        isis 0
            interface "NET_{data["hostname"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
            exit
        exit
        isis {data["isis-a-area"]}
            interface "NET_{data["hostname"]}_{data["network-a"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 100
                exit
            exit
        exit
        ldp
            interface-parameters
                interface "NET_{data["hostname"]}_{data["network-a"]}"
                exit
            exit
        exit
"""
    return(txt)
def make_farend2(data):
    txt=f"""
configure
    port {data["port-b2"]}
        description "NET_{data["far-end-b"]}:{data["port-b2"]}:{data["port-b-type"]}:{data["hostname"]}:{data["port-b1"]}:10GE"
        ethernet
            mode network
            mtu 2102
            collect-stats
            network
                collect-stats
            exit
            hold-time up 5
            ssm
                no shutdown
            exit
            egress-port-qos-policy "NQ_VFQ_IXR_PORT_QOS"
        exit
        no shutdown
    exit
    router Base
        interface "NET_{data["hostname"]}_{data["network-b"]}"
            address {increment_last_octet(data["network-b"])}/31
            port {data["port-b2"]}
            ingress
                qos "NQ_VFQ_IXR_Net_Ing"
            exit
            egress
                egress-remark-policy "NQ_VFQ_IXR_Eg_Remark"
                vlan-qos-policy "NQ_VFQ_IXR_VLAN_QOS"
            exit
            no shutdown
        exit
        isis 0
            interface "NET_{data["hostname"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 200
                exit
            exit
        exit
        isis {data["isis-b-area"]}
            interface "NET_{data["hostname"]}_{data["network-b"]}"
                level-capability level-1
                hello-authentication-key VFQatar
                hello-authentication-type message-digest
                interface-type point-to-point
                level 1
                    hello-interval 10
                    metric 200
                exit
            exit
        exit
        ldp
            interface-parameters
                interface "NET_{data["hostname"]}_{data["network-b"]}"
                exit
            exit
        exit
"""
    return(txt)

def make_poc2(data):
    txt=f"""
ssh chrisnanda.ent@{data["POC2-1"]}
configure 
    router 
        bgp
            group "CSR-POC3-lbgp-ipv4"
                neighbor {data["system"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
exit all
ssh chrisnanda.ent@{data["POC2-2"]}
configure 
    router 
        bgp
            group "CSR-POC3-lbgp-ipv4"
                neighbor {data["system"]}
                    family label-ipv4
                    authentication-key VFQatar
                exit
exit all
"""
    return (txt)
def make_poc1(data):
    ssh1 =""
    ssh2 =""
    if data["POC3-1"] and data["POC3-2"] == "192.168.64.1" "192.168.64.4":
        ssh1 = "172.16.240.7"
        ssh2 = "172.16.240.42"
    else:
        ssh1 = "172.16.240.8"
        ssh2 = "172.16.240.41"
    txt=f"""
ssh chrisnanda.ent@{ssh1}
configure 
    router 
        bgp
            group "Seamless_l3vpns_mp_ibgp"
                neighbor {data["loopback"]}
                    vpn-apply-import
                    import "l3vpn_MBH_Import_IXR_ISIS{data["isis-a-area"]}"
                    export "l3vpn_MBH_Export_IXR_ISIS{data["isis-a-area"]}"
                exit
exit all
ssh chrisnanda.ent@{ssh2}
configure 
    router 
        bgp
            group "Seamless_l3vpns_mp_ibgp"
                neighbor {data["loopback"]}
                    vpn-apply-import
                    import "l3vpn_MBH_Import_IXR_ISIS{data["isis-a-area"]}"
                    export "l3vpn_MBH_Export_IXR_ISIS{data["isis-a-area"]}"
                exit
exit all
"""
    return (txt)
