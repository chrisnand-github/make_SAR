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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                    match "configure service vprn <55000>"
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
            profile "default"
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                entry 50
                    match "password"
                    action permit
                exit
                entry 60
                    match "show config"
                    action deny
                exit
                entry 65
                    match "show li"
                    action deny
                exit
                entry 66
                    match "clear li"
                    action deny
                exit
                entry 67
                    match "tools dump li"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 75
                    match "state"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action permit
                exit
                entry 90
                    match "enable"
                    action permit
                exit
                entry 100
                    match "configure li"
                    action deny
                exit
            exit
            profile "Operator"
                default-action permit-all
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
            exit
            profile "Monitoring"
                default-action deny-all
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
                entry 4
                    description "Monitor service"
                    match "monitor service id"
                    action permit
                exit
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
            profile "OLD_Image_del"
                default-action deny-all
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
                entry 1
                    match "file"
                    action permit
                exit
            exit
            profile "administrative"
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        kill-session
                        lock
                        validate
                    exit
                exit
                entry 10
                    match "configure system security"
                    action permit
                exit
                entry 20
                    match "show system security"
                    action permit
                exit
                entry 30
                    match "tools perform security"
                    action permit
                exit
                entry 40
                    match "tools dump security"
                    action permit
                exit
                entry 42
                    match "tools dump system security"
                    action permit
                exit
                entry 50
                    match "admin system security"
                    action permit
                exit
                entry 100
                    match "configure li"
                    action deny
                exit
                entry 110
                    match "show li"
                    action deny
                exit
                entry 111
                    match "clear li"
                    action deny
                exit
                entry 112
                    match "tools dump li"
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
                password "$2y$10$TU7wk8PQqmzGlq1JYX7aU.2yeF5F9DpmMGNg4MWEgY8WQFMWNNEs."
                access console ftp snmp
                console
                    member "default"
                    member "administrative"
                exit
                snmp
                    authentication none
                exit
            exit
            user "Agata.ANDERSON"
                password "$2y$10$BJsYZ4x6I80AVWgVX2pEs.QSU4hgyYcQ5L0z9OIQ6h/nyFeY47KYG"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Anindito.ent"
                password "$2y$10$EDeSfBHhvRYkKm9g3a072.bgKHJOiyVR/EGC7XaYDiKDdOKkcDqVa"
                access console ftp
                console
                    member "default"
                    member "ARCH2"
                exit
            exit
            user "ArturWen.NOK"
                password "$2y$10$gqSyaxA8merh4K4Wgonc..Z3Im4KLArPwS4MLPaZCyIWnQL20utZm"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "AsmaA"
                password "$2y$10$M6Ka4IcLI.2wSds3/m9Cs.H6.LWSdIDu3zYmT/CQEFGI/g4RmleUG"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "Ayathulla"
                password "$2y$10$tMtbcpVgG.Pr3mzCCPkn2.Ip6fxA/KnVPCrg7r2frPQkqnIvOGjpC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "BartlomiejP "
                password "$2y$10$L1zu5ReaClu41ss6EyGqw.Hes6p9BeWijG4yAqjSxd4sEp3FGRPxy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "BerkayAkar.NOK"
                password "$2y$10$q179VyycTmUULvOOWQOIc.uhQaF5GVpC62pshvvvVZlnsHCcQ6GUi"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Emreoznok"
                password "$2y$10$vMstwKacNXzRKvgxAVla..jEmgHNjI2jrce/McPBsTlIwo3eLuche"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Imiga"
                password "$2y$10$MAPUEpD6AvQ4rjYB7X2F..5bTBREt7yUee2lGVEzhHciMu.AwpLIK"
                access console ftp
            exit
            user "Jakub.Nokia"
                password "$2y$10$pI2NKIhv2xOwwY2qDLSBE.W.1HQPAnxKJ5dIRosESxVqGGOt14Biy"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Mariusz.Bielawski"
                password "$2y$10$UNzUeRgl1pKUllYfVwoS6.hVbA1W/5YWrQMctkccZjqjPPae1F99K"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "Maryia.PAULOVICH"
                password "$2y$10$lo4wx44y2u5Ixt5Dy5J8..O00fQxYP7aA3mnnnoP8ZdsQCoE.4TaW"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Michal.STAFIEJ"
                password "$2y$10$BTTQJfONy.tKKEj8HJiiE.vDkWPMi1CpbehMYOQXu2F8Aw6VlgJx."
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "MichalJakub.NOK"
                password "$2y$10$.JVHU5tQDMtMTzbWGpGDU.uFs8GU5TmvWvqfqHsCxjXyNIJWtVQu6"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Milosz.JACOSZEK"
                password "$2y$10$rJzEAIdb9/FZc7nzyHOY6.0Jf.IK3mCeImgbdmFFuQCiVzMqSjBci"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Mohammedel.Nok"
                password "$2y$10$ElEMCjiS/I.lzu24eOZ.M.AuiRsBhyKbDz9Mkt019qJ7pSsmXxC6K"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Noemi.Izydorek"
                password "$2y$10$Pj8D5Swh88bV2xBYEzZz2.zoXvc0o1UVBncd8VG9d6gisqprotnn2"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "PawelSzys.NOK"
                password "$2y$10$CBlAC2GTCdhYWdD4mPYts.hAv/sQB6Re/VDNiZRF2k3qNonP3KO4q"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Sandi "
                password "$2y$10$tqAE3Cve6dcH2B6Q/FTa6.Addl0N2fNvUWqpors8dImEKH8.UYuE6"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "SlawomirO"
                password "$2y$10$y1ubw/0nIC.xYEluhIy8Y.ucdDuCiWZo.MdXtj73c19KwYGui8.Y6"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.arajeeb"
                password "$2y$10$4pNIJfWaNOhOkB3qwP7Qk.8AOES4RC3hr15.xA6JS/1/8ULcprJCC"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "aanoop"
                password "$2y$10$f2.bB8/zSxkZ75IRiHeWY.oN0k0Aods96djlD4R6Raaam9G3NjiDS"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "abdel"
                password "$2y$10$ojSXBTItvFGm9n8UjKSzI.n.8EhiJOIdD237YF7aItWxeFNpqix0q"
                access console ftp
            exit
            user "admin"
                password "$2y$10$Z3X.TUNZetb11cdPMnrM2.IolIsZMS3bLHI/okLD5Y2WA/BJzAsFO"
                access console ftp
                console
                    member "administrative"
                exit
            exit
            user "adnank"
                password "$2y$10$bL9EnwjviFwz4Ci3.i2QE.K5JkOkcZnwNxAW6pd2BhxJ6ODqKniWy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ahmad"
                password "$2y$10$w.x6s3XSWlWgY9vboIhrI.B9YavUo6C4WLuWKWWMH5hTt2o9L1lfu"
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ahmedm"
                password "$2y$10$X9CF4nSS3QAXdhuXE4qPM./QcY97HjFrcvUakkyAngAm5NTJFLqYG"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "ajain"
                password "$2y$10$weIpbX1pqElnetSF50wEs.7pzNlHiJqLkoJ65C4FWkSetnokdClbW"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ajay"
                password "$2y$10$53WYFeMyQNpvY/JeWNXAk.ctMynAO7WzB0nmkqsozye6z5HnsIFXW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ajith"
                password "$2y$10$yn/I/ae3etGMzKupdVZGA.Djs1IPPyVwaj8n1PfXagAIuWaSu3QXC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "akram"
                password "$2y$10$jEJXoVZCLyvceLXl.WsWc.GX1DG94juugjR3x76L5oyO6tlsTiAu6"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "amand"
                password "$2y$10$QluyW8vr99oVS4ZTWfXNI.s2vdJJxKWdZaUd8/i6dW/9Bcya6iIKW"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "ameer"
                password "$2y$10$F9h9gp.ThtTj0KIwBV/Zg.wA7Q3I1p7YpSNKC0lFv6mdXnfHSDaJW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ameers"
                password "$2y$10$GTtQM.VL2IBhZPNeT0NDo.oQ10CztV7xurLBVl2EPV.yw7j0UHUJC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "amitht"
                password "$2y$10$ENcwQGZVpxo0vJ.6giSLQ.0si4l5Isohs.aXn.tlRcjUqicPPxjX."
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "amogh.acharya"
                password "$2y$10$xPKsvT6fPRsONUKJiqy/g.msTFubPKigS9nd5gGIjz4u4Ghsz09QS"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "anas.hammami"
                password "$2y$10$HHRFSQ7EuX9gqtSE2yz9s.jKSxHzv3NhWYFHManKgHw92WF1D0ipm"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "aprajitar"
                password "$2y$10$ksKEgwjk/CzxboIuCuurI.m6WRlFgn/3uM.zoOKrypuxda/jUvncW"
                access console ftp
                console
                    no member "default"
                    member "show"
                exit
            exit
            user "arnas"
                password "$2y$10$A3nJLcTA5/h4cJuhvrDbI.09VBvyY8J0kbXtV.HBkhe884QnWd.Ju"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "aryak"
                password "$2y$10$MAcItbTBFQdIVj/cbVPAc.hJUQKTv6ra2Pu994wGJ5rmXEFFsa37K"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "asaadawi"
                password "$2y$10$PB.MuQsDHLx.6.iNVf8ro.hOUzflyzSSlc89RXW9taz9tRdw87qAi"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ashok.a"
                password "$2y$10$ZjrVuJe3LmZCtrrVv1O92.5qvgYX/eng5RP4B4lXEq3Lhg18m3LnG"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "ashwanid"
                password "$2y$10$T.0VgfA0.ffLjnurRIHV2.IsCt8Q640PtcAG/P8Ai7M2Yy6wDQyqu"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ashwanik"
                password "$2y$10$H..DMr2qVJGiH1hCpFh/E.Jcthy4ZGu3pJQf7UXEvdH9xoxGUh6q6"
                access console ftp
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "atanu"
                password "$2y$10$l6uTE7TKOfDtv2j9cg7PE.AL50eWMiQbZY0LuCnbxDOOsi/qtPrPy"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ataray"
                password "$2y$10$/49eON/Y/Zk8oI10BDX8Q.CZHD3Cf7JVZEtLfYDpIIWniSy3B.Fii"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ayathulla"
                password "$2y$10$JM7gKNiHWl6M0sHIW1yKY.ecq1Z/Qc3HcEH14IN2n1rE1LyUuc73W"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "ayman"
                password "$2y$10$wwL/38lFPGxLNccNxfr9M.DeR/NiFBr/gCltsWu9xY1iIY7yZdlbu"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "babar"
                password "$2y$10$ruf0BBe1MDX1LnHeGHXZ2.97KPH1mMWTdqLLVFBv/pQvTR4TS1LsS"
                access console ftp
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "bartu.balkis"
                password "$2y$10$tIJoc5oaiuQhWDcoSvJvg.DMtVUbFz6e5KtkhO3H/WZdrPq5S25zC"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "bbohdano"
                password "$2y$10$lyxmVY00Aefj7gD3n2v86.HoZK2T4Zq4Z6FqI74hQ6rPSjuhffVfq"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "benhard"
                password "$2y$10$GJKV/iMXm07U35PpVHrBs.Dr8fDMhdIQWudgZIFVjhywhVEhH.ltK"
                access console ftp
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "blaxmi"
                password "$2y$10$gsmr638OXAQIjgBgz/KC6.6/5OzgtguWZr1PLnyjLPS3X3Dc.lszS"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "carl"
                password "$2y$10$piDCG6GrBHn/yhqUANM8E.4i1glwZD1lhe7WA4rqUUNH7c4aXNZtm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "chaitanya"
                password "$2y$10$J4tB3jITliJdtGytjC4bM.SuI/cjSjN5Z6.JOun4qqmES2XHWSUUe"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "chandana"
                password "$2y$10$Uusm76p7NSfqUPR5rD6UA.d25KMYIjoKLe1n28fI2iTk2CvUt85Je"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "chittick"
                password "$2y$10$fpRFQvcUlnaCdvMlCC5jE.igouBO78lXvyjWnEFAthBpAHiA7F6l."
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "chrisnanda.ent"
                password "$2y$10$Pf57RGxUf0KA/fXip6/q6.eDXQaondixVjMDHNp5qohCLTwsWjB2e"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "darutkow"
                password "$2y$10$xHVGSgOA/lZe8UtNRIb2Q.rIiCTmVagUgZOXOBT0gxepZq6QYuabW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "datchu"
                password "$2y$10$zyxZetKidQFrCTLgr3WSI.kwqg6QdpwcpYZ1mSKm7qE0rqvDAlL9."
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "deepu.jena"
                password "$2y$10$kHpMDUb8tqJEQHus.WXg2.JoNTCOOGNFx0.VzIEE1th2rYptw7ZDe"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                    member "OLD_Image_del"
                exit
            exit
            user "deni.sartika"
                password "$2y$10$lpTdH1y/mIAUVB/hE7n92.YkUSl6ZyRqW4grjvP8H/OWENG0YMd5W"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "dikshantv"
                password "$2y$10$beKWqA98to4bhxHlok7nU.97zEGJLb58DlxfuOn9e7BILqScSACue"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "dille"
                password "$2y$10$GGiJaK/a9XSDD5bcL4dPw.EVjfDAsNrw4vmKLEFNgzWlftDpXjLCu"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "dilo.ayarmali"
                password "$2y$10$M415WWt3T2qF52XFBg/0A.cx4xKqnc5sMAi.MW3zaU4e0Jkk2sDMa"
                access console ftp
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "dragos"
                password "$2y$10$bQtZAXmwCrRTdoz8BJJio.TrDXJc4ctWtHOy1dtF4zQiBLHpkZFTS"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "dragos.serban"
                password "$2y$10$jCzY2cSCqEK9V1wC./cSg.KvLBSR2X.Ynemkg6ILndn0ii9bmbwWC"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "eijas"
                password "$2y$10$siaif03kMhieNyXjZUolc.ZPzjt7Ooa9BgEl45EtcflCQftqVQEXS"
                access console ftp snmp
                console
                    member "Operator"
                    member "default"
                exit
                snmp
                    authentication none
                exit
            exit
            user "elshandawily"
                password "$2y$10$h2y75bghUuIHGqR9COQMM.dTS8vvDuXoGd9vjqSFZykwtBjdaUvd."
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "emrek"
                password "$2y$10$xPpS5ugkLeRfeEmlt732A.9ixstEyHh1ocKAOUDSWiIJFYWNPpXlC"
                access console ftp
                console
                    no member "default"
                    member "TPM"
                exit
            exit
            user "gems.bo"
                password "$2y$10$YBV1cY4PnPmbRHyT5vSMM.zChdQy3lf2vdG/.ZqF3Z8RBr/oTOW2S"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "gnocipfo"
                password "$2y$10$QgudhT1Z71LK6I77kCYpQ.ImyF/MqYaTXWAhWtviD6F6347iB4ZVu"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "gomaa"
                password "$2y$10$lpGQcDM264F/a7HzWb3H6.r21rRbnDVjL45.xr1m2tvg6VdVljXje"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "hakim.nokia"
                password "$2y$10$b/k.zBsRhzMnlIWdhi6LY.2fW37AZUUGXjhOU2ZhMhhD78MNlihOy"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "hamed"
                password "$2y$10$eT3n3IAxapi14yjNuQXg..sqi417rdrLHiqIkcnDFhQuIrooXSDiK"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "hhanafy"
                password "$2y$10$.bTmFnfegmyUQEdVNVVqA.M79wf/ra/4X6UVecAysAuZydehBgKaK"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "hwasilew"
                password "$2y$10$fdhZTU9T3pR7/AsNMtyys.IbP5pc7DGwUl4Pcx6R2FfzubXZFxS7W"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "iakhtar"
                password "$2y$10$Xu.fyYpOiI3mJpRBeIS8Y.P.bkXOcIgNsxfdMgdPxbt6S1juRUFvq"
                access console
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "irfana"
                password "$2y$10$IITwJ129DhCMMvBIh6Zic.DN0UyZVq864eyMgHtlcwnqeUQ9vn/hm"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "ishan.sood"
                password "$2y$10$gEd8r6yyxepkcLOnLAWqY.n0sTWjH7goeacaHJjikvYtLkCqY/7Z2"
                access console ftp
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "jaka"
                password "$2y$10$2m42kYLc6MSa4/zT6mdzk.bLJNaMNupeLLjffxp2XhAKbxX43qJr2"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "jaka.ets"
                password "$2y$10$SltSmzEIzmwbZzTUCM.zM.plBhhVqRhA3rxg3reQ8JDwvriXDLHzW"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "jdorsz"
                password "$2y$10$h31DCcFcKkbaC2W7tLRPE.iyiJ2qMEH5jyKJlX26HND85xd.ZL5K6"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "kallawym"
                password "$2y$10$twBUQ/d.fr8R5vjaAxMjM.ubr0ouHbwFYgUpxM1xhQd9ER11cYR4i"
                access console ftp
            exit
            user "kannann"
                password "$2y$10$MCatS/tP91RSjuF3.idiE.9SfGLOLNJ5HktxK3xaGjHELKdDRqUv2"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "karinau"
                password "$2y$10$SV3tS6Wh0r6cBBncLsfDY.Kru50Uy7JBwTLHHiY3xcu8V9kAN7QBm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "kashif"
                password "$2y$10$9SABguABnkhrjVsN1pF9o.qCRfjvC9pwpw0TlM5b0v.PJNdofGl7G"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "komals"
                password "$2y$10$bFcgMFznpSvZ7XsjYSpWo.3M1Pgf8Imgl7rVfTJL09pUhYzgeGq4G"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "labid"
                password "$2y$10$1F57UtdLmAT.w5.ZT00ls.fwMJuak5ZbTXDihLgGdmwlGJ3iqSQnW"
                access console
                console
                    new-password-at-login
                    member "SOC"
                    member "default"
                exit
            exit
            user "lmiga"
                password "$2y$10$a1yvwJl2TWXWWcFAQnDmo.G6uoAIeHuUof0rE6wifW/KnE9ZVwoIK"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "logger"
                password "$2y$10$3glIzz74h25r1SJ6c5AJA.wglV373pyWQCHrTyV0RHQ.ckYurd4/y"
                access ftp
                console
                    cannot-change-password
                exit
            exit
            user "lpraveen"
                password "$2y$10$VI5sQaBVXJv8/ZQDhquj6.OxHFz5pj2gCgWrjgjDWC2T2apWumUHm"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "lwitkows"
                password "$2y$10$m9Z8qsXGfYD/ixrleMM/E.r3J.ssp1LH1W0wLBX9fdPQD1RAjrbYG"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "madel1"
                password "$2y$10$IQ/1Bjxo5VSv9G/UtNObE.s0hehZzpkMlBkM/0.OKJbgcM0FJAEs2"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "mahendra.dixit"
                password "$2y$10$LOn2bmu4TQV3FzLj6v3mw.Qyw3d7BKhkJbuPPJgD5eqel8/Mn97oa"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "maheshk"
                password "$2y$10$BD4wlDQ4.hv3qBSU5EPGE.hFknAzvZKLa0xf2FaOxcM1Purrnc1Yu"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "mahmed"
                password "$2y$10$0GcEipQoVOpoi8kzKXxWM.30vtshzeIGylE2uYJyWIzZKyBGOStTK"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "manojk"
                password "$2y$10$TFm.cNiqL2b6XtOQjr5c6.Glg8rb8FBDDoK9nIpggmOvoHL7g/n12"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "mczerwin"
                password "$2y$10$GQBk3Wmk92V8HBXrO7GoY.onFwdZescSeFnOJQrJ/8hWLSyJk7itC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mdevi"
                password "$2y$10$P5UAwDy8VjXVXLornDReA.i..tA2XqjaIqugmSgO3dq9ia5w59G.u"
                access console
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "medjarab"
                password "$2y$10$v4MpUQqgX1SnDUmkKvhWg.adQHvetwVjyh0xHC6FTcmtK12w8iFiy"
                access console ftp
                console
                    member "default"
                    member "show"
                exit
            exit
            user "medjerab.mohamed"
                password "$2y$10$bwhhFgxDC6WuB632qf6jE.OQ54KjxAR9fSxKvo8xt1IUMZY1xbxYW"
                access console ftp
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "mercy"
                password "$2y$10$aDS3swcRKPchm04hKqPvc.UI5IgMoMuGpsyQKnvfBh7YN45Zrdn/y"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mjaber"
                password "$2y$10$T93bjGkxhmcnbWRoF928M.glv3GEG2Z9ARLTffaNPci/.YMVXwwP2"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mkallawy"
                password "$2y$10$Aii/oTIZE1Be49IcMgQtk.oKwfnq4w6RPDIw0C0WeksAAm4f9HaKC"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "mnadeem"
                password "$2y$10$O1VfE7slyW4ai4utcGWnw.7XlAu8Z1wEZIDcOpmqMnTqiANDTSR/m"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "mnowako"
                password "$2y$10$WQJWm1NWxV6UXcxOky24c.O0vCOr.MXrvEQFOl2EbzJJuLzIbibpC"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "mohamedn"
                password "$2y$10$q2.qk5Rt301yrfY4KUg0E.6Ux8eQ8CUq2KMJidO4TTZyn.T6sMnrS"
                access console ftp
                console
                    new-password-at-login
                    no member "default"
                    member "administrative"
                exit
            exit
            user "monikandan"
                password "$2y$10$m3rxk8G3.LPhLEpn.U4lk.utlhFB70/L8XsdFWFP2I9GEIzowjzki"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "muchlisi"
                password "$2y$10$l.f25Q9K9YqaSxbDdUhGA.OTU82xzUD.ZhE4dyE8PkJmw5oUlwQAq"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "muhammad.ehsan"
                password "$2y$10$XNFZsEpQZv82.wc45OUsI.HDPoZqcbLi2JtOgqJVLPXjdNjY/pHey"
                access console ftp
                console
                    member "Operator"
                    member "default"
                exit
            exit
            user "muhammad.khalid"
                password "$2y$10$XrS8Jdkp8WF1T9GMNYHQI.mj2t9YkPmAexy0Wp2j7vKjVNrOO2Q5C"
                access console ftp
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "muhammad.khan1"
                password "$2y$10$hlcspdckFx9rmtI0O2xUI.xkTfdQNe32JrRCh8MsBg0mNYiXoD4XS"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "muksharm"
                password "$2y$10$/nI4tqJ2eUhmEWQFtVJdU.1AXyWjeX6yBc/IX1nfC3jc7p/khHjSq"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "nader"
                password "$2y$10$X5syQIaxlG4n7CncWXj8A.pj1I6jhbg4yPQWk0fiZoI/mfUh7MecO"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "naser"
                password "$2y$10$wWspJ7GdCyNA4qaJ.e/Hw.5NQjPZyKRGL.XOhmhfMSvNdls7nJKWG"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "nebackup"
                password "$2y$10$bckph6X18pbap7PKE.pts./NheinF2ws3vMfZ4hhhcF87lyIOh0jC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "nokia-project"
                password "$2y$10$RZm6h4mUDs6gxeOQWAheY./31OYyZhAl/Mc7bAxYx671dR8MFYclO"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "nokiaproject"
                password "$2y$10$ujlZE/Dt6PAq1867wGXek.u5kXiYgQn1nYdg0S.sKX3R2IJWeWAj6"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "nokiatac"
                password "$2y$10$al58LDgeGNSmtuIB/DigA.atlNmBmQfr3W.Vvy9A4.ZkiQ46taa4a"
                access console ftp
                console
                    member "default"
                    member "show"
                exit
            exit
            user "ocesmeci"
                password "$2y$10$L.K46duvivkgr2FjpzJXs.Nwl51wygQqiiCqf0bO1Zh.xXAb5opYG"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "onursari"
                password "$2y$10$29NvfxIGwzQ7FOttP6hwU.12PLpYDAkxTB1RATlmGwJVsNPSb7Jx2"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ozges"
                password "$2y$10$UPlpYcDjuyAnDn0iIAeEU.zlcvwZVtM6Gmh8B..CriwM.fP1lMIQu"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "patrick"
                password "$2y$10$mvQpDaqJDjBUijZUkG6oM.ZgvZdAJ.sN.qSYBDVYj8MD/d9H.0dNi"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "pawelc"
                password "$2y$10$G2c2zWaagtHl7UYo8dNXo.sGMLcdJwce/fBnldzqUlYCLOvoVEBI6"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "phaldar"
                password "$2y$10$LJEa8xZoEpQwjd3Alu3Qg.h93WlTI7GIZrbqvoN.Gc32t9OR4c6US"
                access console
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "philippeg"
                password "$2y$10$/t1xey3UapTMNVjLYSlBU.Kkkw0My6JZKfkmTOC2dvHrj8C0FcKH6"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "priyankac"
                password "$2y$10$owWDqXndr1a5tnhsW96UM.jGcmzqxgoktIAEc7vIWys1Xegl5PhSe"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "psingh"
                password "$2y$10$d3bQvanqqIlDmIwuZg8gg.DtBAZs0p649xlkxlyri7Jm622ex7Rea"
                access console
                console
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "rahul"
                password "$2y$10$WmBL6HlhvqNPSQFel1tK6.xZJWYU2V0dzL1H0wEZispXvuMLNtTUq"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rais.majada"
                password "$2y$10$GiIXI8BJqDi8.eRqV9QXY.hZ38bXrq7FSNzVvqE6sar/lDz9jawfW"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rashmir"
                password "$2y$10$ChpmLQ6/RbcgtXTMCgQqI.lYpF4QkvLLXTVdM5h1Lared9GXB1bAC"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "rbaluni"
                password "$2y$10$9E1p3AG0gl.4FV0EyC.Fw.J/QgMGVUP5kPNwcAGZirQGhW61j6IjK"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rishi.ksingh"
                password "$2y$10$bJIfI3yEkju5gl.PuVk9A.Cw4dGBuJ2PVaKFBmfb1vBH.wYAKAoee"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "rohit.mishra.huawei"
                password "$2y$10$cqOviqjGUSXCKIxE9gC.k.1yNCeUgSWKNMYmJwpj384HdDBOr5R.e"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rohit.sharma"
                password "$2y$10$0JirAy.YP9KoYzgn4noOM.6GbsaEP43jxdE.ebfMioTmbDTnWaQXe"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rohitb"
                password "$2y$10$Aos9ejHHNmIqhGg0l36Pw.JmQmQdemJCx1Txlo523u25dSpVyt4gW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rojowt"
                password "$2y$10$fKI7fwJhb83j1vdd7.S0E.SXW6GZhVB.ctznRvADKxyPL56Fm69De"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "saadawya"
                password "$2y$10$tvJtmL6.p4ZKHQUz6Memc.n28mBgDsWiT8pCpk2b.HDkzLWoOkep."
                access console ftp
                console
                    new-password-at-login
                    member "VF-NSU"
                    member "default"
                exit
            exit
            user "sachin.ip"
                password "$2y$10$lBbgPQ8Mx2v3cR353Pn0E.SbwjzVJyewwr8UwpGEjcBzyk0t1mwjO"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "saik"
                password "$2y$10$rQvDaPBNXktFuRYYH19MA.zOtwdp9AOAkV5xc1wVnXKG/JkA79igy"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "sajeert"
                password "$2y$10$/WnqbaI8G3/5y2/1Kd8.A.y7vwAnDvwgCCW.SqUrcfuRKfqLvPjnO"
                access console ftp
                console
                    member "administrative"
                    member "default"
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
            user "sandeep.lamba"
                password "$2y$10$taxaklLzfBqfaSdJPH4qI.2XsD8/OwgXMHIBSq2WLuWaDG4RYUjea"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "sandi"
                password "$2y$10$G.P4CGffeHdluIV1nV2hw.thWTKXY1D5RdzknjcsGXyS5rpSiVgWS"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "santosh.nokia"
                password "$2y$10$wyJ59ILMq/KMxNmZfvMyA.X4vAHx8lbl02GKj54T9lTk.gtpws5zm"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "scp_user"
                password "$2y$10$GyUElJbJh7YVq14mseanM.rp2K2jb/EyoVwvREmQofoz19c3/p//K"
                access console ftp
                console
                    cannot-change-password
                exit
            exit
            user "senem.akpunar"
                password "$2y$10$X4FglvgZyL.c6brnBmF3o.kgHSRxUQGA.kVEm9U2161Hd8W42.2Oi"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "sgopal"
                password "$2y$10$g2AZB5wvieCu7fIoGMPu6.WmS5.gZmbbEYdxiG1qZXo6ZgFo09Q46"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "shamidb"
                password "$2y$10$4QouKWgJ0hN/ZKxXiLH/M.PSDiZqKTn/p87HrPZo9cZ1PpaMjBzqW"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "sherif"
                password "$2y$10$6.x1E4FJWq4M6ZpBdcjMY.457T81DbFE62mtc0PCuHHaSQ7tOesV6"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "sherifg"
                password "$2y$10$ejwFUeWESIqXoILC.HPrw.uky0YjrI.Nl27YVk/qSbWP9P4ofIJoq"
                access console ftp
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "sivak"
                password "$2y$10$Rr7KRcoN9iiT97olR5da..yhTc3vSodeGqMpomhmH.Dn3Zdz/jfnO"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "snmpv3user"
                password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
                access snmp
                snmp
                    authentication hash2 hmac-sha1-96 tY6e30qGjaS99vSGKARRWihDaOKFGo+n2+QIxQviefIFbM+k privacy cbc-des yfo1jywYbmtc8v7rkqrSrXKLM9xX5LxhMdz8uOybbcw=
                    group "nmsPriv"
                exit
            exit
            user "srinivasalu"
                password "$2y$10$fc/dMYM0uVpceMiWIbc86.JOzzj8MhAK/iB5URbi9/dHPgc5jxMsW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ssoyasan"
                password "$2y$10$dr.hkStubY5NDcZByWmVw.dWiE/Boz2q2RkiV7422mwktxIFJuvBu"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "subheep"
                password "$2y$10$OMkOondtIqRkw/s6nXtVM.GIIFapMpqNhI.Oj736L87nDrT5vY6oK"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "sudhanshu"
                password "$2y$10$YZ5yR4ZcE2qsoG6o/ZVXQ.vvkQ3LKkM/lz5jESysbcs4sDL2Vnwzq"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "sujith"
                password "$2y$10$.gCuz7jJgsgZQghQJA7ck.TbGr9dRpu/lijX7Zz/g5Ln.gUYc1Joe"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "svenkat"
                password "$2y$10$xjSPCU4rVOnNbSiMDFeY6.0.EMB1l./RsH3XhxVhWsRGpeg1gYBd."
                access console
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "swghosh"
                password "$2y$10$IrEpEh9BpTTiI/5m10GEs.6FmAGH/KkZIY24S2W9bG68H5gGOa.3C"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "syeda"
                password "$2y$10$7xfLGrQbiirOuAQx7XaSk.WHA.puw1fgxOK7T7M8CpUGO3/8klZOG"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "tarekc"
                password "$2y$10$Loa0h0q.K6xUa7obAkFJE.0iRLJpRqBftdDeeMFxiqyD5AnjWCEFu"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "tcoban"
                password "$2y$10$HR9WVQ3Vc2/kvnwlD4HJk.cXHAThp1L7LcQjm2IMPz.1f0r1UZa56"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "test"
                password "$2y$10$eIeDtQmlauMQH.Vnot5dU.i3Vr3mkcN7qWDLjI3G6EMRjLsKoCJdi"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vfq.mali"
                password "$2y$10$j9d1xmi6JajRCmybR5XGI.TId./PXYvtCJFmMEZyvPerLp62mkdGS"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vfqsoc"
                password "$2y$10$gBN6VSLtg5oZVvg5kG1I2.71uuNvsitKqlKtXJ/iwMaGotVRFNjZ6"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "vijay.singh"
                password "$2y$10$A4Zf8ymra7A5nJ6rx9EGU.l/bP99LfgTj/ymqjcz57KLx7MWtQmaC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vinodk"
                password "$2y$10$G712VrbUEuDqdhCchWmP2.T0foQ7CT2VGnTGsoy8AZ08HghWk79uy"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "vishaldeep"
                password "$2y$10$BzC250Jxr6toYGecdz35o.AOUWcpDSQJokujF1bcYnzFwhaS6ixzW"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "vivekk"
                password "$2y$10$wyA.4IpBIk00hqgCIXECc.X9i1Ia41vqmPfv4/lkgdr3hXjRhMYiu"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "vkumar"
                password "$2y$10$6zn/hhdJGC8P3vyeJC6KY.vSjB47bMAmPfpVvFM1cIDYu9DshZLUu"
                access console
                console
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "wslomins"
                password "$2y$10$d.y/52/4KZ93hW4eVF2g2.udnTtyAGyUqC.AbkdTdQq8gLrHMV3gq"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "yousef"
                password "$2y$10$rWyxoqxAWrqIe.vR.iWKY.MLdWdoHmBBQXAFWEeSDXSWUoXwm4zte"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            snmp
                access group "nmsPriv" security-model usm security-level privacy read "iso" write "iso" notify "iso"
                access group "nmsPriv" security-model usm security-level privacy context "vprn" prefix read "vprn-view" write "vprn-view" notify "iso"
                community "toTlp9V2fM4Xlk/6J5lSuWaBLCnT" hash2 r version v2c
                community "cV3ISTw2V5pbEWmVEA9jXgB/1EERXQA=" hash2 rwa version v2c
            exit
            ssh
                preserve-key
            exit
            dist-cpu-protection
                policy "_default-access-policy" create
                exit
                policy "_default-network-policy" create
                exit
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
        vprn 55000 customer 1 create
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
            service-name "ENT-4G-5G_Public"
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                    match "configure service vprn <55000>"
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
            profile "default"
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                entry 50
                    match "password"
                    action permit
                exit
                entry 60
                    match "show config"
                    action deny
                exit
                entry 65
                    match "show li"
                    action deny
                exit
                entry 66
                    match "clear li"
                    action deny
                exit
                entry 67
                    match "tools dump li"
                    action deny
                exit
                entry 70
                    match "show"
                    action permit
                exit
                entry 75
                    match "state"
                    action permit
                exit
                entry 80
                    match "enable-admin"
                    action permit
                exit
                entry 90
                    match "enable"
                    action permit
                exit
                entry 100
                    match "configure li"
                    action deny
                exit
            exit
            profile "Operator"
                default-action permit-all
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
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
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
            exit
            profile "Monitoring"
                default-action deny-all
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
                entry 4
                    description "Monitor service"
                    match "monitor service id"
                    action permit
                exit
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
            profile "OLD_Image_del"
                default-action deny-all
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        validate
                    exit
                exit
                entry 1
                    match "file"
                    action permit
                exit
            exit
            profile "administrative"
                netconf
                    base-op-authorization
                        action
                        cancel-commit
                        close-session
                        commit
                        copy-config
                        create-subscription
                        delete-config
                        discard-changes
                        edit-config
                        get
                        get-config
                        get-data
                        get-schema
                        kill-session
                        lock
                        validate
                    exit
                exit
                entry 10
                    match "configure system security"
                    action permit
                exit
                entry 20
                    match "show system security"
                    action permit
                exit
                entry 30
                    match "tools perform security"
                    action permit
                exit
                entry 40
                    match "tools dump security"
                    action permit
                exit
                entry 42
                    match "tools dump system security"
                    action permit
                exit
                entry 50
                    match "admin system security"
                    action permit
                exit
                entry 100
                    match "configure li"
                    action deny
                exit
                entry 110
                    match "show li"
                    action deny
                exit
                entry 111
                    match "clear li"
                    action deny
                exit
                entry 112
                    match "tools dump li"
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
                password "$2y$10$TU7wk8PQqmzGlq1JYX7aU.2yeF5F9DpmMGNg4MWEgY8WQFMWNNEs."
                access console ftp snmp
                console
                    member "default"
                    member "administrative"
                exit
                snmp
                    authentication none
                exit
            exit
            user "Agata.ANDERSON"
                password "$2y$10$BJsYZ4x6I80AVWgVX2pEs.QSU4hgyYcQ5L0z9OIQ6h/nyFeY47KYG"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Anindito.ent"
                password "$2y$10$EDeSfBHhvRYkKm9g3a072.bgKHJOiyVR/EGC7XaYDiKDdOKkcDqVa"
                access console ftp
                console
                    member "default"
                    member "ARCH2"
                exit
            exit
            user "ArturWen.NOK"
                password "$2y$10$gqSyaxA8merh4K4Wgonc..Z3Im4KLArPwS4MLPaZCyIWnQL20utZm"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "AsmaA"
                password "$2y$10$M6Ka4IcLI.2wSds3/m9Cs.H6.LWSdIDu3zYmT/CQEFGI/g4RmleUG"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "Ayathulla"
                password "$2y$10$tMtbcpVgG.Pr3mzCCPkn2.Ip6fxA/KnVPCrg7r2frPQkqnIvOGjpC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "BartlomiejP "
                password "$2y$10$L1zu5ReaClu41ss6EyGqw.Hes6p9BeWijG4yAqjSxd4sEp3FGRPxy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "BerkayAkar.NOK"
                password "$2y$10$q179VyycTmUULvOOWQOIc.uhQaF5GVpC62pshvvvVZlnsHCcQ6GUi"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Emreoznok"
                password "$2y$10$vMstwKacNXzRKvgxAVla..jEmgHNjI2jrce/McPBsTlIwo3eLuche"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Imiga"
                password "$2y$10$MAPUEpD6AvQ4rjYB7X2F..5bTBREt7yUee2lGVEzhHciMu.AwpLIK"
                access console ftp
            exit
            user "Jakub.Nokia"
                password "$2y$10$pI2NKIhv2xOwwY2qDLSBE.W.1HQPAnxKJ5dIRosESxVqGGOt14Biy"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Mariusz.Bielawski"
                password "$2y$10$UNzUeRgl1pKUllYfVwoS6.hVbA1W/5YWrQMctkccZjqjPPae1F99K"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "Maryia.PAULOVICH"
                password "$2y$10$lo4wx44y2u5Ixt5Dy5J8..O00fQxYP7aA3mnnnoP8ZdsQCoE.4TaW"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Michal.STAFIEJ"
                password "$2y$10$BTTQJfONy.tKKEj8HJiiE.vDkWPMi1CpbehMYOQXu2F8Aw6VlgJx."
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "MichalJakub.NOK"
                password "$2y$10$.JVHU5tQDMtMTzbWGpGDU.uFs8GU5TmvWvqfqHsCxjXyNIJWtVQu6"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Milosz.JACOSZEK"
                password "$2y$10$rJzEAIdb9/FZc7nzyHOY6.0Jf.IK3mCeImgbdmFFuQCiVzMqSjBci"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Mohammedel.Nok"
                password "$2y$10$ElEMCjiS/I.lzu24eOZ.M.AuiRsBhyKbDz9Mkt019qJ7pSsmXxC6K"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Noemi.Izydorek"
                password "$2y$10$Pj8D5Swh88bV2xBYEzZz2.zoXvc0o1UVBncd8VG9d6gisqprotnn2"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "PawelSzys.NOK"
                password "$2y$10$CBlAC2GTCdhYWdD4mPYts.hAv/sQB6Re/VDNiZRF2k3qNonP3KO4q"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Sandi "
                password "$2y$10$tqAE3Cve6dcH2B6Q/FTa6.Addl0N2fNvUWqpors8dImEKH8.UYuE6"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "SlawomirO"
                password "$2y$10$y1ubw/0nIC.xYEluhIy8Y.ucdDuCiWZo.MdXtj73c19KwYGui8.Y6"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.arajeeb"
                password "$2y$10$4pNIJfWaNOhOkB3qwP7Qk.8AOES4RC3hr15.xA6JS/1/8ULcprJCC"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "aanoop"
                password "$2y$10$f2.bB8/zSxkZ75IRiHeWY.oN0k0Aods96djlD4R6Raaam9G3NjiDS"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "abdel"
                password "$2y$10$ojSXBTItvFGm9n8UjKSzI.n.8EhiJOIdD237YF7aItWxeFNpqix0q"
                access console ftp
            exit
            user "admin"
                password "$2y$10$Z3X.TUNZetb11cdPMnrM2.IolIsZMS3bLHI/okLD5Y2WA/BJzAsFO"
                access console ftp
                console
                    member "administrative"
                exit
            exit
            user "adnank"
                password "$2y$10$bL9EnwjviFwz4Ci3.i2QE.K5JkOkcZnwNxAW6pd2BhxJ6ODqKniWy"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ahmad"
                password "$2y$10$w.x6s3XSWlWgY9vboIhrI.B9YavUo6C4WLuWKWWMH5hTt2o9L1lfu"
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ahmedm"
                password "$2y$10$X9CF4nSS3QAXdhuXE4qPM./QcY97HjFrcvUakkyAngAm5NTJFLqYG"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "ajain"
                password "$2y$10$weIpbX1pqElnetSF50wEs.7pzNlHiJqLkoJ65C4FWkSetnokdClbW"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ajay"
                password "$2y$10$53WYFeMyQNpvY/JeWNXAk.ctMynAO7WzB0nmkqsozye6z5HnsIFXW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ajith"
                password "$2y$10$yn/I/ae3etGMzKupdVZGA.Djs1IPPyVwaj8n1PfXagAIuWaSu3QXC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "akram"
                password "$2y$10$jEJXoVZCLyvceLXl.WsWc.GX1DG94juugjR3x76L5oyO6tlsTiAu6"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "amand"
                password "$2y$10$QluyW8vr99oVS4ZTWfXNI.s2vdJJxKWdZaUd8/i6dW/9Bcya6iIKW"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "ameer"
                password "$2y$10$F9h9gp.ThtTj0KIwBV/Zg.wA7Q3I1p7YpSNKC0lFv6mdXnfHSDaJW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ameers"
                password "$2y$10$GTtQM.VL2IBhZPNeT0NDo.oQ10CztV7xurLBVl2EPV.yw7j0UHUJC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "amitht"
                password "$2y$10$ENcwQGZVpxo0vJ.6giSLQ.0si4l5Isohs.aXn.tlRcjUqicPPxjX."
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "amogh.acharya"
                password "$2y$10$xPKsvT6fPRsONUKJiqy/g.msTFubPKigS9nd5gGIjz4u4Ghsz09QS"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "anas.hammami"
                password "$2y$10$HHRFSQ7EuX9gqtSE2yz9s.jKSxHzv3NhWYFHManKgHw92WF1D0ipm"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "aprajitar"
                password "$2y$10$ksKEgwjk/CzxboIuCuurI.m6WRlFgn/3uM.zoOKrypuxda/jUvncW"
                access console ftp
                console
                    no member "default"
                    member "show"
                exit
            exit
            user "arnas"
                password "$2y$10$A3nJLcTA5/h4cJuhvrDbI.09VBvyY8J0kbXtV.HBkhe884QnWd.Ju"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "aryak"
                password "$2y$10$MAcItbTBFQdIVj/cbVPAc.hJUQKTv6ra2Pu994wGJ5rmXEFFsa37K"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "asaadawi"
                password "$2y$10$PB.MuQsDHLx.6.iNVf8ro.hOUzflyzSSlc89RXW9taz9tRdw87qAi"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ashok.a"
                password "$2y$10$ZjrVuJe3LmZCtrrVv1O92.5qvgYX/eng5RP4B4lXEq3Lhg18m3LnG"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "ashwanid"
                password "$2y$10$T.0VgfA0.ffLjnurRIHV2.IsCt8Q640PtcAG/P8Ai7M2Yy6wDQyqu"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ashwanik"
                password "$2y$10$H..DMr2qVJGiH1hCpFh/E.Jcthy4ZGu3pJQf7UXEvdH9xoxGUh6q6"
                access console ftp
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "atanu"
                password "$2y$10$l6uTE7TKOfDtv2j9cg7PE.AL50eWMiQbZY0LuCnbxDOOsi/qtPrPy"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ataray"
                password "$2y$10$/49eON/Y/Zk8oI10BDX8Q.CZHD3Cf7JVZEtLfYDpIIWniSy3B.Fii"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ayathulla"
                password "$2y$10$JM7gKNiHWl6M0sHIW1yKY.ecq1Z/Qc3HcEH14IN2n1rE1LyUuc73W"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "ayman"
                password "$2y$10$wwL/38lFPGxLNccNxfr9M.DeR/NiFBr/gCltsWu9xY1iIY7yZdlbu"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "babar"
                password "$2y$10$ruf0BBe1MDX1LnHeGHXZ2.97KPH1mMWTdqLLVFBv/pQvTR4TS1LsS"
                access console ftp
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "bartu.balkis"
                password "$2y$10$tIJoc5oaiuQhWDcoSvJvg.DMtVUbFz6e5KtkhO3H/WZdrPq5S25zC"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "bbohdano"
                password "$2y$10$lyxmVY00Aefj7gD3n2v86.HoZK2T4Zq4Z6FqI74hQ6rPSjuhffVfq"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "benhard"
                password "$2y$10$GJKV/iMXm07U35PpVHrBs.Dr8fDMhdIQWudgZIFVjhywhVEhH.ltK"
                access console ftp
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "blaxmi"
                password "$2y$10$gsmr638OXAQIjgBgz/KC6.6/5OzgtguWZr1PLnyjLPS3X3Dc.lszS"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "carl"
                password "$2y$10$piDCG6GrBHn/yhqUANM8E.4i1glwZD1lhe7WA4rqUUNH7c4aXNZtm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "chaitanya"
                password "$2y$10$J4tB3jITliJdtGytjC4bM.SuI/cjSjN5Z6.JOun4qqmES2XHWSUUe"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "chandana"
                password "$2y$10$Uusm76p7NSfqUPR5rD6UA.d25KMYIjoKLe1n28fI2iTk2CvUt85Je"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "chittick"
                password "$2y$10$fpRFQvcUlnaCdvMlCC5jE.igouBO78lXvyjWnEFAthBpAHiA7F6l."
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "chrisnanda.ent"
                password "$2y$10$Pf57RGxUf0KA/fXip6/q6.eDXQaondixVjMDHNp5qohCLTwsWjB2e"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "darutkow"
                password "$2y$10$xHVGSgOA/lZe8UtNRIb2Q.rIiCTmVagUgZOXOBT0gxepZq6QYuabW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "datchu"
                password "$2y$10$zyxZetKidQFrCTLgr3WSI.kwqg6QdpwcpYZ1mSKm7qE0rqvDAlL9."
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "deepu.jena"
                password "$2y$10$kHpMDUb8tqJEQHus.WXg2.JoNTCOOGNFx0.VzIEE1th2rYptw7ZDe"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                    member "OLD_Image_del"
                exit
            exit
            user "deni.sartika"
                password "$2y$10$lpTdH1y/mIAUVB/hE7n92.YkUSl6ZyRqW4grjvP8H/OWENG0YMd5W"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "dikshantv"
                password "$2y$10$beKWqA98to4bhxHlok7nU.97zEGJLb58DlxfuOn9e7BILqScSACue"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "dille"
                password "$2y$10$GGiJaK/a9XSDD5bcL4dPw.EVjfDAsNrw4vmKLEFNgzWlftDpXjLCu"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "dilo.ayarmali"
                password "$2y$10$M415WWt3T2qF52XFBg/0A.cx4xKqnc5sMAi.MW3zaU4e0Jkk2sDMa"
                access console ftp
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "dragos"
                password "$2y$10$bQtZAXmwCrRTdoz8BJJio.TrDXJc4ctWtHOy1dtF4zQiBLHpkZFTS"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "dragos.serban"
                password "$2y$10$jCzY2cSCqEK9V1wC./cSg.KvLBSR2X.Ynemkg6ILndn0ii9bmbwWC"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "eijas"
                password "$2y$10$siaif03kMhieNyXjZUolc.ZPzjt7Ooa9BgEl45EtcflCQftqVQEXS"
                access console ftp snmp
                console
                    member "Operator"
                    member "default"
                exit
                snmp
                    authentication none
                exit
            exit
            user "elshandawily"
                password "$2y$10$h2y75bghUuIHGqR9COQMM.dTS8vvDuXoGd9vjqSFZykwtBjdaUvd."
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "emrek"
                password "$2y$10$xPpS5ugkLeRfeEmlt732A.9ixstEyHh1ocKAOUDSWiIJFYWNPpXlC"
                access console ftp
                console
                    no member "default"
                    member "TPM"
                exit
            exit
            user "gems.bo"
                password "$2y$10$YBV1cY4PnPmbRHyT5vSMM.zChdQy3lf2vdG/.ZqF3Z8RBr/oTOW2S"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "gnocipfo"
                password "$2y$10$QgudhT1Z71LK6I77kCYpQ.ImyF/MqYaTXWAhWtviD6F6347iB4ZVu"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "gomaa"
                password "$2y$10$lpGQcDM264F/a7HzWb3H6.r21rRbnDVjL45.xr1m2tvg6VdVljXje"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "hakim.nokia"
                password "$2y$10$b/k.zBsRhzMnlIWdhi6LY.2fW37AZUUGXjhOU2ZhMhhD78MNlihOy"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "hamed"
                password "$2y$10$eT3n3IAxapi14yjNuQXg..sqi417rdrLHiqIkcnDFhQuIrooXSDiK"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "hhanafy"
                password "$2y$10$.bTmFnfegmyUQEdVNVVqA.M79wf/ra/4X6UVecAysAuZydehBgKaK"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "hwasilew"
                password "$2y$10$fdhZTU9T3pR7/AsNMtyys.IbP5pc7DGwUl4Pcx6R2FfzubXZFxS7W"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "iakhtar"
                password "$2y$10$Xu.fyYpOiI3mJpRBeIS8Y.P.bkXOcIgNsxfdMgdPxbt6S1juRUFvq"
                access console
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "irfana"
                password "$2y$10$IITwJ129DhCMMvBIh6Zic.DN0UyZVq864eyMgHtlcwnqeUQ9vn/hm"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "ishan.sood"
                password "$2y$10$gEd8r6yyxepkcLOnLAWqY.n0sTWjH7goeacaHJjikvYtLkCqY/7Z2"
                access console ftp
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "jaka"
                password "$2y$10$2m42kYLc6MSa4/zT6mdzk.bLJNaMNupeLLjffxp2XhAKbxX43qJr2"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "jaka.ets"
                password "$2y$10$SltSmzEIzmwbZzTUCM.zM.plBhhVqRhA3rxg3reQ8JDwvriXDLHzW"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "jdorsz"
                password "$2y$10$h31DCcFcKkbaC2W7tLRPE.iyiJ2qMEH5jyKJlX26HND85xd.ZL5K6"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "kallawym"
                password "$2y$10$twBUQ/d.fr8R5vjaAxMjM.ubr0ouHbwFYgUpxM1xhQd9ER11cYR4i"
                access console ftp
            exit
            user "kannann"
                password "$2y$10$MCatS/tP91RSjuF3.idiE.9SfGLOLNJ5HktxK3xaGjHELKdDRqUv2"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "karinau"
                password "$2y$10$SV3tS6Wh0r6cBBncLsfDY.Kru50Uy7JBwTLHHiY3xcu8V9kAN7QBm"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "kashif"
                password "$2y$10$9SABguABnkhrjVsN1pF9o.qCRfjvC9pwpw0TlM5b0v.PJNdofGl7G"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "komals"
                password "$2y$10$bFcgMFznpSvZ7XsjYSpWo.3M1Pgf8Imgl7rVfTJL09pUhYzgeGq4G"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "labid"
                password "$2y$10$1F57UtdLmAT.w5.ZT00ls.fwMJuak5ZbTXDihLgGdmwlGJ3iqSQnW"
                access console
                console
                    new-password-at-login
                    member "SOC"
                    member "default"
                exit
            exit
            user "lmiga"
                password "$2y$10$a1yvwJl2TWXWWcFAQnDmo.G6uoAIeHuUof0rE6wifW/KnE9ZVwoIK"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "logger"
                password "$2y$10$3glIzz74h25r1SJ6c5AJA.wglV373pyWQCHrTyV0RHQ.ckYurd4/y"
                access ftp
                console
                    cannot-change-password
                exit
            exit
            user "lpraveen"
                password "$2y$10$VI5sQaBVXJv8/ZQDhquj6.OxHFz5pj2gCgWrjgjDWC2T2apWumUHm"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "lwitkows"
                password "$2y$10$m9Z8qsXGfYD/ixrleMM/E.r3J.ssp1LH1W0wLBX9fdPQD1RAjrbYG"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "madel1"
                password "$2y$10$IQ/1Bjxo5VSv9G/UtNObE.s0hehZzpkMlBkM/0.OKJbgcM0FJAEs2"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "mahendra.dixit"
                password "$2y$10$LOn2bmu4TQV3FzLj6v3mw.Qyw3d7BKhkJbuPPJgD5eqel8/Mn97oa"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "maheshk"
                password "$2y$10$BD4wlDQ4.hv3qBSU5EPGE.hFknAzvZKLa0xf2FaOxcM1Purrnc1Yu"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "mahmed"
                password "$2y$10$0GcEipQoVOpoi8kzKXxWM.30vtshzeIGylE2uYJyWIzZKyBGOStTK"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "manojk"
                password "$2y$10$TFm.cNiqL2b6XtOQjr5c6.Glg8rb8FBDDoK9nIpggmOvoHL7g/n12"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "mczerwin"
                password "$2y$10$GQBk3Wmk92V8HBXrO7GoY.onFwdZescSeFnOJQrJ/8hWLSyJk7itC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mdevi"
                password "$2y$10$P5UAwDy8VjXVXLornDReA.i..tA2XqjaIqugmSgO3dq9ia5w59G.u"
                access console
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "medjarab"
                password "$2y$10$v4MpUQqgX1SnDUmkKvhWg.adQHvetwVjyh0xHC6FTcmtK12w8iFiy"
                access console ftp
                console
                    member "default"
                    member "show"
                exit
            exit
            user "medjerab.mohamed"
                password "$2y$10$bwhhFgxDC6WuB632qf6jE.OQ54KjxAR9fSxKvo8xt1IUMZY1xbxYW"
                access console ftp
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "mercy"
                password "$2y$10$aDS3swcRKPchm04hKqPvc.UI5IgMoMuGpsyQKnvfBh7YN45Zrdn/y"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mjaber"
                password "$2y$10$T93bjGkxhmcnbWRoF928M.glv3GEG2Z9ARLTffaNPci/.YMVXwwP2"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mkallawy"
                password "$2y$10$Aii/oTIZE1Be49IcMgQtk.oKwfnq4w6RPDIw0C0WeksAAm4f9HaKC"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "mnadeem"
                password "$2y$10$O1VfE7slyW4ai4utcGWnw.7XlAu8Z1wEZIDcOpmqMnTqiANDTSR/m"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "mnowako"
                password "$2y$10$WQJWm1NWxV6UXcxOky24c.O0vCOr.MXrvEQFOl2EbzJJuLzIbibpC"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "mohamedn"
                password "$2y$10$q2.qk5Rt301yrfY4KUg0E.6Ux8eQ8CUq2KMJidO4TTZyn.T6sMnrS"
                access console ftp
                console
                    new-password-at-login
                    no member "default"
                    member "administrative"
                exit
            exit
            user "monikandan"
                password "$2y$10$m3rxk8G3.LPhLEpn.U4lk.utlhFB70/L8XsdFWFP2I9GEIzowjzki"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "muchlisi"
                password "$2y$10$l.f25Q9K9YqaSxbDdUhGA.OTU82xzUD.ZhE4dyE8PkJmw5oUlwQAq"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "muhammad.ehsan"
                password "$2y$10$XNFZsEpQZv82.wc45OUsI.HDPoZqcbLi2JtOgqJVLPXjdNjY/pHey"
                access console ftp
                console
                    member "Operator"
                    member "default"
                exit
            exit
            user "muhammad.khalid"
                password "$2y$10$XrS8Jdkp8WF1T9GMNYHQI.mj2t9YkPmAexy0Wp2j7vKjVNrOO2Q5C"
                access console ftp
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "muhammad.khan1"
                password "$2y$10$hlcspdckFx9rmtI0O2xUI.xkTfdQNe32JrRCh8MsBg0mNYiXoD4XS"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "muksharm"
                password "$2y$10$/nI4tqJ2eUhmEWQFtVJdU.1AXyWjeX6yBc/IX1nfC3jc7p/khHjSq"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "nader"
                password "$2y$10$X5syQIaxlG4n7CncWXj8A.pj1I6jhbg4yPQWk0fiZoI/mfUh7MecO"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "naser"
                password "$2y$10$wWspJ7GdCyNA4qaJ.e/Hw.5NQjPZyKRGL.XOhmhfMSvNdls7nJKWG"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "nebackup"
                password "$2y$10$bckph6X18pbap7PKE.pts./NheinF2ws3vMfZ4hhhcF87lyIOh0jC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "nokia-project"
                password "$2y$10$RZm6h4mUDs6gxeOQWAheY./31OYyZhAl/Mc7bAxYx671dR8MFYclO"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "nokiaproject"
                password "$2y$10$ujlZE/Dt6PAq1867wGXek.u5kXiYgQn1nYdg0S.sKX3R2IJWeWAj6"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "nokiatac"
                password "$2y$10$al58LDgeGNSmtuIB/DigA.atlNmBmQfr3W.Vvy9A4.ZkiQ46taa4a"
                access console ftp
                console
                    member "default"
                    member "show"
                exit
            exit
            user "ocesmeci"
                password "$2y$10$L.K46duvivkgr2FjpzJXs.Nwl51wygQqiiCqf0bO1Zh.xXAb5opYG"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "onursari"
                password "$2y$10$29NvfxIGwzQ7FOttP6hwU.12PLpYDAkxTB1RATlmGwJVsNPSb7Jx2"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ozges"
                password "$2y$10$UPlpYcDjuyAnDn0iIAeEU.zlcvwZVtM6Gmh8B..CriwM.fP1lMIQu"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "patrick"
                password "$2y$10$mvQpDaqJDjBUijZUkG6oM.ZgvZdAJ.sN.qSYBDVYj8MD/d9H.0dNi"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "pawelc"
                password "$2y$10$G2c2zWaagtHl7UYo8dNXo.sGMLcdJwce/fBnldzqUlYCLOvoVEBI6"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "phaldar"
                password "$2y$10$LJEa8xZoEpQwjd3Alu3Qg.h93WlTI7GIZrbqvoN.Gc32t9OR4c6US"
                access console
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "philippeg"
                password "$2y$10$/t1xey3UapTMNVjLYSlBU.Kkkw0My6JZKfkmTOC2dvHrj8C0FcKH6"
                access console ftp
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "priyankac"
                password "$2y$10$owWDqXndr1a5tnhsW96UM.jGcmzqxgoktIAEc7vIWys1Xegl5PhSe"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "psingh"
                password "$2y$10$d3bQvanqqIlDmIwuZg8gg.DtBAZs0p649xlkxlyri7Jm622ex7Rea"
                access console
                console
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "rahul"
                password "$2y$10$WmBL6HlhvqNPSQFel1tK6.xZJWYU2V0dzL1H0wEZispXvuMLNtTUq"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rais.majada"
                password "$2y$10$GiIXI8BJqDi8.eRqV9QXY.hZ38bXrq7FSNzVvqE6sar/lDz9jawfW"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rashmir"
                password "$2y$10$ChpmLQ6/RbcgtXTMCgQqI.lYpF4QkvLLXTVdM5h1Lared9GXB1bAC"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "rbaluni"
                password "$2y$10$9E1p3AG0gl.4FV0EyC.Fw.J/QgMGVUP5kPNwcAGZirQGhW61j6IjK"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rishi.ksingh"
                password "$2y$10$bJIfI3yEkju5gl.PuVk9A.Cw4dGBuJ2PVaKFBmfb1vBH.wYAKAoee"
                access console ftp
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "rohit.mishra.huawei"
                password "$2y$10$cqOviqjGUSXCKIxE9gC.k.1yNCeUgSWKNMYmJwpj384HdDBOr5R.e"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rohit.sharma"
                password "$2y$10$0JirAy.YP9KoYzgn4noOM.6GbsaEP43jxdE.ebfMioTmbDTnWaQXe"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rohitb"
                password "$2y$10$Aos9ejHHNmIqhGg0l36Pw.JmQmQdemJCx1Txlo523u25dSpVyt4gW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rojowt"
                password "$2y$10$fKI7fwJhb83j1vdd7.S0E.SXW6GZhVB.ctznRvADKxyPL56Fm69De"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "saadawya"
                password "$2y$10$tvJtmL6.p4ZKHQUz6Memc.n28mBgDsWiT8pCpk2b.HDkzLWoOkep."
                access console ftp
                console
                    new-password-at-login
                    member "VF-NSU"
                    member "default"
                exit
            exit
            user "sachin.ip"
                password "$2y$10$lBbgPQ8Mx2v3cR353Pn0E.SbwjzVJyewwr8UwpGEjcBzyk0t1mwjO"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "saik"
                password "$2y$10$rQvDaPBNXktFuRYYH19MA.zOtwdp9AOAkV5xc1wVnXKG/JkA79igy"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "sajeert"
                password "$2y$10$/WnqbaI8G3/5y2/1Kd8.A.y7vwAnDvwgCCW.SqUrcfuRKfqLvPjnO"
                access console ftp
                console
                    member "administrative"
                    member "default"
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
            user "sandeep.lamba"
                password "$2y$10$taxaklLzfBqfaSdJPH4qI.2XsD8/OwgXMHIBSq2WLuWaDG4RYUjea"
                access console ftp
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "sandi"
                password "$2y$10$G.P4CGffeHdluIV1nV2hw.thWTKXY1D5RdzknjcsGXyS5rpSiVgWS"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "santosh.nokia"
                password "$2y$10$wyJ59ILMq/KMxNmZfvMyA.X4vAHx8lbl02GKj54T9lTk.gtpws5zm"
                access console
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "scp_user"
                password "$2y$10$GyUElJbJh7YVq14mseanM.rp2K2jb/EyoVwvREmQofoz19c3/p//K"
                access console ftp
                console
                    cannot-change-password
                exit
            exit
            user "senem.akpunar"
                password "$2y$10$X4FglvgZyL.c6brnBmF3o.kgHSRxUQGA.kVEm9U2161Hd8W42.2Oi"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "sgopal"
                password "$2y$10$g2AZB5wvieCu7fIoGMPu6.WmS5.gZmbbEYdxiG1qZXo6ZgFo09Q46"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "shamidb"
                password "$2y$10$4QouKWgJ0hN/ZKxXiLH/M.PSDiZqKTn/p87HrPZo9cZ1PpaMjBzqW"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "sherif"
                password "$2y$10$6.x1E4FJWq4M6ZpBdcjMY.457T81DbFE62mtc0PCuHHaSQ7tOesV6"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "sherifg"
                password "$2y$10$ejwFUeWESIqXoILC.HPrw.uky0YjrI.Nl27YVk/qSbWP9P4ofIJoq"
                access console ftp
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "sivak"
                password "$2y$10$Rr7KRcoN9iiT97olR5da..yhTc3vSodeGqMpomhmH.Dn3Zdz/jfnO"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "snmpv3user"
                password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
                access snmp
                snmp
                    authentication hash2 hmac-sha1-96 tY6e30qGjaS99vSGKARRWihDaOKFGo+n2+QIxQviefIFbM+k privacy cbc-des yfo1jywYbmtc8v7rkqrSrXKLM9xX5LxhMdz8uOybbcw=
                    group "nmsPriv"
                exit
            exit
            user "srinivasalu"
                password "$2y$10$fc/dMYM0uVpceMiWIbc86.JOzzj8MhAK/iB5URbi9/dHPgc5jxMsW"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ssoyasan"
                password "$2y$10$dr.hkStubY5NDcZByWmVw.dWiE/Boz2q2RkiV7422mwktxIFJuvBu"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "subheep"
                password "$2y$10$OMkOondtIqRkw/s6nXtVM.GIIFapMpqNhI.Oj736L87nDrT5vY6oK"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "sudhanshu"
                password "$2y$10$YZ5yR4ZcE2qsoG6o/ZVXQ.vvkQ3LKkM/lz5jESysbcs4sDL2Vnwzq"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "sujith"
                password "$2y$10$.gCuz7jJgsgZQghQJA7ck.TbGr9dRpu/lijX7Zz/g5Ln.gUYc1Joe"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "svenkat"
                password "$2y$10$xjSPCU4rVOnNbSiMDFeY6.0.EMB1l./RsH3XhxVhWsRGpeg1gYBd."
                access console
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "swghosh"
                password "$2y$10$IrEpEh9BpTTiI/5m10GEs.6FmAGH/KkZIY24S2W9bG68H5gGOa.3C"
                access console ftp
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "syeda"
                password "$2y$10$7xfLGrQbiirOuAQx7XaSk.WHA.puw1fgxOK7T7M8CpUGO3/8klZOG"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "tarekc"
                password "$2y$10$Loa0h0q.K6xUa7obAkFJE.0iRLJpRqBftdDeeMFxiqyD5AnjWCEFu"
                access console
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "tcoban"
                password "$2y$10$HR9WVQ3Vc2/kvnwlD4HJk.cXHAThp1L7LcQjm2IMPz.1f0r1UZa56"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "test"
                password "$2y$10$eIeDtQmlauMQH.Vnot5dU.i3Vr3mkcN7qWDLjI3G6EMRjLsKoCJdi"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vfq.mali"
                password "$2y$10$j9d1xmi6JajRCmybR5XGI.TId./PXYvtCJFmMEZyvPerLp62mkdGS"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vfqsoc"
                password "$2y$10$gBN6VSLtg5oZVvg5kG1I2.71uuNvsitKqlKtXJ/iwMaGotVRFNjZ6"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "vijay.singh"
                password "$2y$10$A4Zf8ymra7A5nJ6rx9EGU.l/bP99LfgTj/ymqjcz57KLx7MWtQmaC"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vinodk"
                password "$2y$10$G712VrbUEuDqdhCchWmP2.T0foQ7CT2VGnTGsoy8AZ08HghWk79uy"
                access console ftp
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "vishaldeep"
                password "$2y$10$BzC250Jxr6toYGecdz35o.AOUWcpDSQJokujF1bcYnzFwhaS6ixzW"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "vivekk"
                password "$2y$10$wyA.4IpBIk00hqgCIXECc.X9i1Ia41vqmPfv4/lkgdr3hXjRhMYiu"
                access console ftp
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "vkumar"
                password "$2y$10$6zn/hhdJGC8P3vyeJC6KY.vSjB47bMAmPfpVvFM1cIDYu9DshZLUu"
                access console
                console
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "wslomins"
                password "$2y$10$d.y/52/4KZ93hW4eVF2g2.udnTtyAGyUqC.AbkdTdQq8gLrHMV3gq"
                access console ftp
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "yousef"
                password "$2y$10$rWyxoqxAWrqIe.vR.iWKY.MLdWdoHmBBQXAFWEeSDXSWUoXwm4zte"
                access console ftp
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            snmp
                access group "nmsPriv" security-model usm security-level privacy read "iso" write "iso" notify "iso"
                access group "nmsPriv" security-model usm security-level privacy context "vprn" prefix read "vprn-view" write "vprn-view" notify "iso"
                community "toTlp9V2fM4Xlk/6J5lSuWaBLCnT" hash2 r version v2c
                community "cV3ISTw2V5pbEWmVEA9jXgB/1EERXQA=" hash2 rwa version v2c
            exit
            ssh
                preserve-key
            exit
            dist-cpu-protection
                policy "_default-access-policy" create
                exit
                policy "_default-network-policy" create
                exit
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
            port 1/1/5
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
            port 1/1/5
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
        vprn 55000 customer 1 create
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
            service-name "ENT-4G-5G_Public"
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
echo "ISIS (Inst: 1) Configuration"
#--------------------------------------------------
        isis 1
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
                    action deny
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
            exit
            profile "ARCH"
                default-action deny-all
                entry 1
                    match "ping"
                    action permit
                exit
                entry 2
                    match "monitor"
                    action permit
                exit
                entry 3
                    match "configure service"
                    action permit
                exit
                entry 4
                    match "show"
                    action permit
                exit
                entry 5
                    match "oam"
                    action permit
                exit
                entry 6
                    match "configure port"
                    action permit
                exit
                entry 7
                    match "traceroute"
                    action permit
                exit
                entry 8
                    match "ssh"
                    action permit
                exit
                entry 9
                    match "telnet"
                    action permit
                exit
                entry 10
                    match "info"
                    action permit
                exit
                entry 11
                    match "back"
                    action permit
                exit
                entry 12
                    match "admin save"
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
                    match "configure service"
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
            profile "NokiaNSDC"
                default-action deny-all
                entry 2
                    match "admin display-config"
                    action permit
                exit
                entry 3
                    match "show "
                    action permit
                exit
            exit
            profile "Monitoring"
                default-action deny-all
                entry 4
                    description "Monitor service"
                    match "monitor service id"
                    action permit
                exit
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
            profile "OLD_Image_del"
                default-action deny-all
                entry 1
                    match "file"
                    action permit
                exit
            exit
            password
                authentication-order local tacplus radius
                complexity-rules
                    required lowercase 1 uppercase 1 numeric 1 special-character 1
                exit
            exit
            user "Abdullaalnajjar.VFQ"
                password "$2y$10$..Kzx/Z8iTaIlCjOJpOPU.0397TEmuVxASrFfwgtC74IyYJX5oMcm"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "AdminSAM5620"
                password "$2y$10$7u6hg0Epij3/i8eUNE91s.lhvjFL8Mfcef0PxYcB29ClGNB6i2VBK"
                access console ftp snmp 
                console
                    member "default"
                    member "administrative"
                exit
                snmp
                    authentication none
                exit
            exit
            user "Agata.ANDERSON"
                password "$2y$10$D/qKvhlnZCgibSWRq8wgg.aYYdfAs6DuviZ.xwv9wR3EiERxxHri2"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Anindito.ent"
                password "$2y$10$ka90/CtNdZ/faaLSJGHUw.szGjwdv5OEsfKTfpWPPOuo9ATsNT11u"
                access console ftp 
                console
                    member "default"
                    member "ARCH2"
                exit
            exit
            user "Arnas.ent"
                password "$2y$10$FG6N/tfOl9h/GI7dsEs/g..wQTGksJpeiejqZMbOPq.6VmNSdOXZe"
                access console ftp 
                console
                    member "default"
                    member "ARCH2"
                exit
            exit
            user "AsmaA"
                password "$2y$10$M6Ka4IcLI.2wSds3/m9Cs.H6.LWSdIDu3zYmT/CQEFGI/g4RmleUG"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "Ayathulla"
                password "$2y$10$s/GMCJYUsu8iBHVCq1h16.8Dt9ThcfRmwRiBpR8ZF25GnNAQq0UXe"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "BartlomiejP "
                password "$2y$10$W9O7fKJ4ZE5hoZ2DKRGaM.7to9SQvQm8LStkGt3hDhjjtboJTLg9q"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "Emreoznok"
                password "$2y$10$7gg0rP8UYWLKbzl3HLppA.2TPdhTOFEdqmSSmd5dbwrbnrpVgiTyS"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Imiga"
                password "$2y$10$c8MRQ7z6f6y2gGo/96vdc.YIYcfyVqDs0wHRgUeF9Nj0Rb/6g7Mvm"
                access console ftp 
            exit
            user "Mariusz.Bielawski"
                password "$2y$10$ozwC9QUYLqJiHVBeXmbhY.J34oxx5GqbrhOcZxdsg5rI7vBjED4o."
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "Maryia.PAULOVICH"
                password "$2y$10$ZRJhO9RG.BfiiydYRmX8M.mJCIOK3gMZoByRUrxq1L3Nm68epjHyy"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Michal.STAFIEJ"
                password "$2y$10$feVCiGWwUSvJEO5oYlam..slNLjEydeDSTRXEZkCvfIgoi8FhUv9y"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Milosz.JACOSZEK"
                password "$2y$10$oGnPx6EDluLgiWizJEvdw.iRkr4vWyoGirzmV6HvO/7Ly75HGR.ei"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Mohammedel.Nok"
                password "$2y$10$ZWp5iLvGpn.b3qy6F8BCA.mFObirxR/612nQn0B9FPxJfn2aKZgmC"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "Noemi.Izydorek"
                password "$2y$10$AAl17tloEXP.fh3wQ7E.g.MkpEvC0r0uDfulMpSyfElkWw2wRXjbC"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "Sandi "
                password "$2y$10$tqAE3Cve6dcH2B6Q/FTa6.Addl0N2fNvUWqpors8dImEKH8.UYuE6"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "SlawomirO"
                password "$2y$10$o61DaS893oJZKG3jidI7k.baIAZZla4HTrr.HwBwU2.Z7.nWUaspS"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.arajeeb"
                password "$2y$10$QKJ3lo0CTuQaUzUUFaY9c.mwmhLvyTcy/U4Xl/3MF3Kyu4lWUX7Jq"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "VFQ.uwaheed"
                password "$2y$10$ZRcRWeo3JtpG4aKXY6W2E.YS7BBQR1ESo3RKsGLiV/9Y9iHBzYkKG"
                access console 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "aanoop"
                password "$2y$10$f2.bB8/zSxkZ75IRiHeWY.oN0k0Aods96djlD4R6Raaam9G3NjiDS"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "abdel"
                password "$2y$10$Ae8G1xDZxxwr.kbtAi0w..9sXWg/.RPWC6q0ukaQp665XjU2YElCG"
                access console ftp 
            exit
            user "admin"
                password "$2y$10$QarhuT7JaOw9Z6rTP0x8Q..p6ayYwKJwfEJdymEF1Vozl6b1odgim"
                access console ftp 
                console
                    member "administrative"
                exit
            exit
            user "adnank"
                password "$2y$10$0h.akWF5gyhtmfqQHgMoM.msU7VqU/BNCm71.bXBDHOha440Nmj2a"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ahmad"
                password "$2y$10$bwO0QuRTAQVXydtZiMUWE.UkIQOhezfbbW7LcxuD0q/w8PNr1nf.."
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ahmedm"
                password "$2y$10$X9CF4nSS3QAXdhuXE4qPM./QcY97HjFrcvUakkyAngAm5NTJFLqYG"
                access console ftp 
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "ajain"
                password "$2y$10$as2uLUUThcl52tMBl/HwE.7CXfXjQAJNSTTjXcZAKa/cD5z1Y4e.6"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ajay"
                password "$2y$10$53WYFeMyQNpvY/JeWNXAk.ctMynAO7WzB0nmkqsozye6z5HnsIFXW"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ajith"
                password "$2y$10$yn/I/ae3etGMzKupdVZGA.Djs1IPPyVwaj8n1PfXagAIuWaSu3QXC"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "akram"
                password "$2y$10$t4DY0brObRYdF3tlivMgw.iCJ8rm2jY5iKZUC/cb92Pz43xKc4QIW"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "amand"
                password "$2y$10$CD1CwDk6jcbXTJ2olhz9M.h17lBzivy6S/KlNspOByrKEMHatcw1."
                access console ftp 
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "ameer"
                password "$2y$10$F9h9gp.ThtTj0KIwBV/Zg.wA7Q3I1p7YpSNKC0lFv6mdXnfHSDaJW"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ameers"
                password "$2y$10$pbtEEDUHNv40zIyK4E2R2.HehsoSWS1yKbnwnVmsl.CuT..p7ghSG"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "amitht"
                password "$2y$10$ptsW/Ct5poPzEqUonk0hQ.oAhnZF/ZADXT8sN59kMk1sLzI/Vf0Cu"
                access console ftp 
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "amogh.acharya"
                password "$2y$10$XGHh4xJCgbfYblpqGSP0I.be8Q5bGF9ssh8E.R6lM98e47VeGay46"
                access console 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "amr.hanafy"
                password "$2y$10$PoYMH5YP7HF9l/h.JBEjM.38fUvWVExiaG12q03JHx0ZGtlfXLYYS"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "anas.hammami"
                password "$2y$10$.kfzUu6g5pk0fAcVguYwE.TL1td1Rr6ZNMdbGAz9Wg4FRz9fGDb6u"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "aprajitar"
                password "$2y$10$PF1AyNORcQZbkq4RdUBNc.PkVDcF/Cqb4Eg2J2SAmRuLk59uIXSLG"
                access console ftp 
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "arnas"
                password "$2y$10$A3nJLcTA5/h4cJuhvrDbI.09VBvyY8J0kbXtV.HBkhe884QnWd.Ju"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "arslan.pervaiz"
                password "$2y$10$ENkn9jtwEks4cfXCJ83dk.4INcE0HODYh62kZsTJafk/8tvB3UaTy"
                access console 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "aryak"
                password "$2y$10$MAcItbTBFQdIVj/cbVPAc.hJUQKTv6ra2Pu994wGJ5rmXEFFsa37K"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "asaadawi"
                password "$2y$10$H5tig0vuOemH754qyjAhk.C85F.Ee.0vb1jVQxfC1SL0KlNVov4X."
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ashok.a"
                password "$2y$10$KOBclN59yUWlkBBBicuoM.qmoHfDyAH4zkiAUq1mMsH8P0BwH84Za"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "ashwanik"
                password "$2y$10$PtOXLyJ6h7yN89GmTNOBw.17up9dKbWTIDxLeX9q0AfDJgakwV0x2"
                access console ftp 
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "atanu"
                password "$2y$10$J6iPU3CmvLtvzR6RbarnE.dd39sMmXeUqarKNJP45F6aIHlRPqAlq"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "ataray"
                password "$2y$10$/49eON/Y/Zk8oI10BDX8Q.CZHD3Cf7JVZEtLfYDpIIWniSy3B.Fii"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "ayathulla.mv"
                password "$2y$10$BoxilMsIARYxhzuFamE3E.QS/vcsaNJFmGRWN7qUq32zO/LsjFh7y"
                access console ftp 
                console
                    new-password-at-login
                    no member "default"
                    member "administrative"
                exit
            exit
            user "ayman"
                password "$2y$10$OGMhxlArlaRn9bPPep8I..eL8w/.3gyh8bFuFXi9R8lOY/fBNHePe"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "ayman.ets"
                password "$2y$10$GhMgR1V74QmRoMz2rs9ak.T2EeYUujyl8OVPUgFnRMa03ncdb4bCO"
                access console ftp 
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "babar"
                password "$2y$10$2Ozq/P8D6dn2odfRF7zWk.6VwDYdaxClf0vhUz9bCzMyDRyMyUATS"
                access console ftp 
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "bangashm"
                password "$2y$10$e4AObhZIwO/amiyySprAU.zBSjbjiwTgSU29Mq9ctmnY.h55Eii3y"
                access console 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "bartu.balkis"
                password "$2y$10$KnWCmS8sNM0i2/Ywf04kE.y8jhoTt5Qtor.QQhbguye0NYIOs2cwy"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "bbohdano"
                password "$2y$10$lyxmVY00Aefj7gD3n2v86.HoZK2T4Zq4Z6FqI74hQ6rPSjuhffVfq"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "benhard"
                password "$2y$10$BFs629TicZY5AjulDayrY.NRjCO42fU8dfsko6u/K7OAImgHcO7pG"
                access console ftp 
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "blaxmi"
                password "$2y$10$gsmr638OXAQIjgBgz/KC6.6/5OzgtguWZr1PLnyjLPS3X3Dc.lszS"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "carl"
                password "$2y$10$h4KXXlKNiQMoCGRLSlaek.SMv9pubxxIWZohd9v78itQD8UHk.MIm"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "ceren"
                password "$2y$10$kxubyUKYc1/858F35Ii3U.UF50e7aWQFdfvyGlMVNiRZOH4OCEbn."
                access console ftp 
                console
                    member "default"
                    member "ARCH2"
                exit
            exit
            user "chaitanya"
                password "$2y$10$J4tB3jITliJdtGytjC4bM.IPa.jnbFZW3YRkEkQpm2A/Bk59zCZKq"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "chandana"
                password "$2y$10$umCNcoz8H33LC2nZOjhI2.etHaSILl1yVfmxBCvWiIxMnPh3zT5aW"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "chittick"
                password "$2y$10$fpRFQvcUlnaCdvMlCC5jE.KIhCiIGkKj.GYowWQNZR7oHaHkiGi3m"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "chrisnanda.ent"
                password Nokia@123
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "darutkow"
                password "$2y$10$xHVGSgOA/lZe8UtNRIb2Q.rIiCTmVagUgZOXOBT0gxepZq6QYuabW"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "datchu"
                password "$2y$10$zyxZetKidQFrCTLgr3WSI.kwqg6QdpwcpYZ1mSKm7qE0rqvDAlL9."
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "deepu.jena"
                password "$2y$10$SppJvxBnsfMY1Jcmsj/fY.P1wbdQTfbIWcK6bN1nIV/n0VcazWmiS"
                access console ftp 
                console
                    member "Monitoring"
                    member "default"
                    member "OLD_Image_del"
                exit
            exit
            user "deni.sartika"
                password "$2y$10$KfnoBCok6qq0BlWw9XEqo.eHN16IT64/vxPoX.MBFCZzk9S0S0e6e"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "dikshantv"
                password "$2y$10$beKWqA98to4bhxHlok7nU.97zEGJLb58DlxfuOn9e7BILqScSACue"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "dille"
                password "$2y$10$GGiJaK/a9XSDD5bcL4dPw.EVjfDAsNrw4vmKLEFNgzWlftDpXjLCu"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "dilo.ayarmali"
                password "$2y$10$pgU01LOoBe2TLqOM6guqQ.bv4mjr25EQ2XhoM8GIKJL1jtWY.bXLq"
                access console ftp 
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "dragos"
                password "$2y$10$bQtZAXmwCrRTdoz8BJJio.TrDXJc4ctWtHOy1dtF4zQiBLHpkZFTS"
                access console ftp 
                console
                    member "default"
                    member "show"
                exit
            exit
            user "dragos.serban"
                password "$2y$10$vZjUpLwKYwVf24otf6CQE.DOgyIcBcbxlSUzKsjaR/2nxuF.I5gJm"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "eijas"
                password "$2y$10$uKrhLMVTbJiQjn1h41xWs.zUklntNROzKYMftdxBWyrWFNur4h9du"
                access console ftp snmp 
                console
                    member "Operator"
                    member "default"
                exit
                snmp
                    authentication none
                exit
            exit
            user "elshandawily"
                password "$2y$10$AGn6.ASik3nkRCwgkEOGY.eGBPBJT2ZTJUlCPDxeM3Qq55zMuS0sq"
                access console ftp 
                console
                    member "default"
                    member "show"
                exit
            exit
            user "emre.ent"
                password "$2y$10$wuUTtaqSZyslBKP67yWbo.kwEKIBtxbncMMg52pXZZpQPTSchxITC"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "gems.bo"
                password "$2y$10$sm0lko/WiAiRvrtw/m1SU.rWld/obwOj62fMy.Y0iAJzlyNpN84CC"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "gnocipfo"
                password "$2y$10$9uEAyfW1kSGO3mB1VC7Y2.SSwda8V0rRSH4zIOFIJrnzGkUAveKqG"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "gomaa"
                password "$2y$10$lpGQcDM264F/a7HzWb3H6.r21rRbnDVjL45.xr1m2tvg6VdVljXje"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "hakim.nokia"
                password "$2y$10$DZjnIOqGD3ID4nF/fhUnw.Py8Mzyx3/BLPS1eRTdb62WQs04rrpNO"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "hamed"
                password "$2y$10$eT3n3IAxapi14yjNuQXg..sqi417rdrLHiqIkcnDFhQuIrooXSDiK"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "hardik.pandya"
                password "$2y$10$ii/HcYS/VLIsvIXwuEdqY.RpiPH5VHnOC9ft5tNN.BLyitU8cBute"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "hhanafy"
                password "$2y$10$.bTmFnfegmyUQEdVNVVqA.M79wf/ra/4X6UVecAysAuZydehBgKaK"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "huseyin.ent"
                password "$2y$10$0NK4gH3GufZvgOXEtGbjY.qsbpimAQsovlKp5rgTUMNW/pXEsTC4a"
                access console ftp 
                console
                    member "default"
                    member "ARCH2"
                exit
            exit
            user "hwasilew"
                password "$2y$10$fdhZTU9T3pR7/AsNMtyys.IbP5pc7DGwUl4Pcx6R2FfzubXZFxS7W"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "iakhtar"
                password "$2y$10$gk/pUuUhRF5avPRqkgRwA.WCbRukLmiw7c7w.NLBofhx/F.2zC2Rq"
                access console 
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "irfana"
                password "$2y$10$MyE9/lFYc1E6o2lSCAqcs.K4HUtJGECDALBUHv9.rGruBrQG1cgfO"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "ishan.sood"
                password "$2y$10$6a0S669.yaZuMqAEzfMEc.v3cQpuwOTn8tKj5amUuvwH5ZWcJhxJG"
                access console ftp 
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "jaka"
                password "$2y$10$9g6UZJ.zu2AmPbkNrGetU.eTbSa.UDHzwgL10VVekRnjaNgG89XM2"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "jaka.ets"
                password "$2y$10$OKpVbkqE.1fAb2Ywtteag.WM7TdVWoLxPUFwqyk6wUsSXOuRwIT2W"
                access console ftp 
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "jakub"
                password "$2y$10$Du/3g9EJkmBD6wSit2dgk.wYYU.dLCAe2Pzy0jxRa5.u9hcqAfeBu"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "jakub.ext"
                password "$2y$10$i4o7Oxw1TMIRs1zO2YEfw.AwsE0PRVCMVQS9olXlIoiR/7UPogWKi"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "jdorsz"
                password "$2y$10$h31DCcFcKkbaC2W7tLRPE.iyiJ2qMEH5jyKJlX26HND85xd.ZL5K6"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "kallawym"
                password "$2y$10$twBUQ/d.fr8R5vjaAxMjM.ubr0ouHbwFYgUpxM1xhQd9ER11cYR4i"
                access console ftp 
            exit
            user "kannann"
                password "$2y$10$MCatS/tP91RSjuF3.idiE.9SfGLOLNJ5HktxK3xaGjHELKdDRqUv2"
                access console ftp 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "karinau"
                password "$2y$10$CkwxMXYNVXHkQoO0ggVmA.IZC9KKjNvDHeX0zpiEXBeBqylJFK14a"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "kashif"
                password "$2y$10$9SABguABnkhrjVsN1pF9o.qCRfjvC9pwpw0TlM5b0v.PJNdofGl7G"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "komals"
                password "$2y$10$E9L3fp6jLmLadnodq/XY6.h3iLEU3cA/cwbqf0GSxIFCoUHYEMKPm"
                access console ftp 
                console
                    new-password-at-login
                    no member "default"
                    member "administrative"
                exit
            exit
            user "krzysztof"
                password "$2y$10$3CkL//.lKeEcZt9JdZSY2.QRJbqwkBlCMFE7guazqOnEi4m7bkX0."
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "labid"
                password "$2y$10$UL8Gzv524266MH4YJK5XA.ids6L/lQZ/bHp.SOuUPWUkLDPoR0vju"
                access console 
                console
                    new-password-at-login
                    member "SOC"
                    member "default"
                exit
            exit
            user "lpraveen"
                password "$2y$10$VI5sQaBVXJv8/ZQDhquj6.OxHFz5pj2gCgWrjgjDWC2T2apWumUHm"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "lwitkows"
                password "$2y$10$m9Z8qsXGfYD/ixrleMM/E.r3J.ssp1LH1W0wLBX9fdPQD1RAjrbYG"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "madel1"
                password "$2y$10$IQ/1Bjxo5VSv9G/UtNObE.dZr09UzKEL3tLseWFJxMFHYW5.rp24a"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "mahendra.dixit"
                password "$2y$10$mX25uGKvgGsubG28J6FDI.7cllFdUJYHH4GfzsUieFwI6TYGLRP.u"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "maheshk"
                password "$2y$10$BD4wlDQ4.hv3qBSU5EPGE.hFknAzvZKLa0xf2FaOxcM1Purrnc1Yu"
                access console ftp 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "mahmed"
                password "$2y$10$0GcEipQoVOpoi8kzKXxWM.30vtshzeIGylE2uYJyWIzZKyBGOStTK"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "manojk"
                password "$2y$10$TFm.cNiqL2b6XtOQjr5c6.Glg8rb8FBDDoK9nIpggmOvoHL7g/n12"
                access console ftp 
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "mariusz"
                password "$2y$10$.Lx.7tUqKf.lGtxBj9p8s..SsMRnK5Kg8vXAdGedNH3xPuflxX166"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mczerwin"
                password "$2y$10$GQBk3Wmk92V8HBXrO7GoY.onFwdZescSeFnOJQrJ/8hWLSyJk7itC"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mdevi"
                password "$2y$10$06mTqovNCiirPX/4NGHMs.MKiVhWA9XjMg.0hhn.nqLtWzKubwQsy"
                access console 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "medjarab"
                password "$2y$10$b8n/DWbHgfhTo7uqQEw7E.PCsL3Bdf82sIB8fNw4GwiIroCE0BKE6"
                access console ftp 
                console
                    member "default"
                    member "show"
                exit
            exit
            user "medjerab.mohamed"
                password "$2y$10$rPgX34Iz4r/5imYh2PBmE.so.pJQ7mEDkRv4laeBOdaAVrdfbgyLW"
                access console ftp 
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "mercy"
                password "$2y$10$aDS3swcRKPchm04hKqPvc.UI5IgMoMuGpsyQKnvfBh7YN45Zrdn/y"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mjaber"
                password "$2y$10$T93bjGkxhmcnbWRoF928M.glv3GEG2Z9ARLTffaNPci/.YMVXwwP2"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "mkallawy"
                password "$2y$10$Aii/oTIZE1Be49IcMgQtk.oKwfnq4w6RPDIw0C0WeksAAm4f9HaKC"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "mnadeem"
                password "$2y$10$O1VfE7slyW4ai4utcGWnw.7XlAu8Z1wEZIDcOpmqMnTqiANDTSR/m"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "mnowako"
                password "$2y$10$WQJWm1NWxV6UXcxOky24c.O0vCOr.MXrvEQFOl2EbzJJuLzIbibpC"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "mohamedn"
                password "$2y$10$q2.qk5Rt301yrfY4KUg0E.6Ux8eQ8CUq2KMJidO4TTZyn.T6sMnrS"
                access console ftp 
                console
                    new-password-at-login
                    no member "default"
                    member "administrative"
                exit
            exit
            user "muchlisi"
                password "$2y$10$14rgWf4SW3aETU.cPZowU.74E8W.H3diiOEnazpw2C9xGNgplWzHK"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "muhammad.ehsan"
                password "$2y$10$VvDYmdCbjfs.1dwCr88pA.O1h9mTuWSCXvi2aZiQ5pQnXbf2eLEdS"
                access console ftp 
                console
                    member "Operator"
                    member "default"
                exit
            exit
            user "muhammad.khalid"
                password "$2y$10$8h.XXfn34YrZEb5wRyWwk.iF2bdewJdsissZt1hPcwqVvP4y0UH4a"
                access console ftp 
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "muhammad.khan1"
                password "$2y$10$oEuWDGm52o30jZTVHJxAY.1/NwDOCLvQ6HWG7V/e1QVKuH5MX/UMy"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "muksharm"
                password "$2y$10$pscL1nKeNUwDyEHPCBdJQ.xVw9KnSdgqBdJNXLtZB36yV4HHycsmG"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "nader"
                password "$2y$10$X5syQIaxlG4n7CncWXj8A.pj1I6jhbg4yPQWk0fiZoI/mfUh7MecO"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "naser"
                password "$2y$10$wWspJ7GdCyNA4qaJ.e/Hw.CxNNmlXBieLJDFP3y.2NFVsAOFH6NRC"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "nebackup"
                password "$2y$10$bckph6X18pbap7PKE.pts./NheinF2ws3vMfZ4hhhcF87lyIOh0jC"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "nikhil.garg"
                password "$2y$10$1y15NcvuPKtBjtrVzQaN2.RvkCa3kRZkQfa9hlcav2dIbXwSjVsWK"
                access console snmp 
                console
                    member "default"
                    member "Monitoring"
                exit
                snmp
                    authentication none
                    group "nmsNoAuth"
                exit
            exit
            user "nikhil.garg1@huawei.com"
                password "$2y$10$54gxD/8ebxFfCyChyCfl..y4BjKKP0GItV.KHw52hjtGIASWbidSy"
                access console snmp 
                console
                    member "default"
                    member "Monitoring"
                exit
                snmp
                    authentication none
                    group "nmsNoAuth"
                exit
            exit
            user "noemi"
                password "$2y$10$2kS1kYDLvsK1kZqJ.YNb6.oamF.k/ry4WK.OYmDKJtdGlTapJHeUq"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "nokia-project"
                password "$2y$10$atKj..HrhiBQZ6V2B2Oi..dMDCqxAignAwJJ63MCzs6FJviT54il."
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "nokiaproject"
                password "$2y$10$ZAs0Rsa1oJZvgQctUeRo2.bTqA9f5MeIP5IctvcAcRKQspScJgK/S"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "nokiatac"
                password "$2y$10$BsRWxxVPH2BzVaZ5QS5jQ.xHTRM66gcZOEz/hk8llNAosmURbz4y."
                access console ftp 
                console
                    member "default"
                    member "show"
                exit
            exit
            user "osamah"
                password "$2y$10$S9ZXRAGsl2Ynie.LO/qok.SMxsbz4ImXDzMdNf4hV3VanJYCLYCAS"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "patrick"
                password "$2y$10$mvQpDaqJDjBUijZUkG6oM.ZgvZdAJ.sN.qSYBDVYj8MD/d9H.0dNi"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "pawel.nsdc"
                password "$2y$10$mjsy1HT2vdQ1esn0eZfIs.CRi2Z55j/yay7jD8hgV4Tqt6qqoH8N."
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "pawelc"
                password "$2y$10$E5CRMlihMrRKHfphMHBrs.664epxVBqkNhfVkGtPGEwjl.N0c976i"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "phaldar"
                password "$2y$10$1a4yaT3ykOc13wtyLy7IY.HSvZ4Gyq9YzJz4OF3dq8QHaY0yaNj/m"
                access console 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "philippeg"
                password "$2y$10$/t1xey3UapTMNVjLYSlBU.Kkkw0My6JZKfkmTOC2dvHrj8C0FcKH6"
                access console ftp 
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "priyankac"
                password "$2y$10$mIZ8ZANhoJZjMAVSVFLoE.Evyg9V7Tn.2d15YjpLztfMIA3zgotIu"
                access console ftp 
                console
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "psingh"
                password "$2y$10$d3bQvanqqIlDmIwuZg8gg.DtBAZs0p649xlkxlyri7Jm622ex7Rea"
                access console 
                console
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "rafalb"
                password "$2y$10$fh/GyWmje9gIz1G/pWztk./xEPclOUiK69Smq6aW3JW1nuWipopTq"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rahul"
                password "$2y$10$WmBL6HlhvqNPSQFel1tK6.xZJWYU2V0dzL1H0wEZispXvuMLNtTUq"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rahuls"
                password "$2y$10$598V.keXt/gWqdvdN72RE.Co6zL/18qznisFik.F8sCCi5a.WXtXm"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rais.majada"
                password "$2y$10$Fg8ReqsECtgmYjfdLBVWM.Xc9BEb/y6Z7Dm5EQorvRWsp4k7hSMd."
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rashmir"
                password "$2y$10$nkri76r/XYOnmnWwggnXU.ITx1niqZBsgErUTX2jsTxZm/2zoazXm"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "rbaluni"
                password "$2y$10$9E1p3AG0gl.4FV0EyC.Fw.J/QgMGVUP5kPNwcAGZirQGhW61j6IjK"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rishi.ksingh"
                password "$2y$10$5DmS5sOgX9Sq5WDn3rsF6.ZIRVajCQJXAIp8e2Da0pNbpcwq3fmcy"
                access console ftp 
                console
                    new-password-at-login
                    member "Monitoring"
                    member "default"
                exit
            exit
            user "rohit.mishra.huawei"
                password "$2y$10$FQiLFCjiaf/U9nt9AFW4c.1mqAwSDIpR1hwYEj67smBSMCdg4YsG."
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "rohit.sharma"
                password "$2y$10$9aN7mjPLru4PhloaUTQRo.l9tLH4vrZuk/x0SbC04GaERYgsV6zNK"
                access console ftp 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "rohitb"
                password "$2y$10$1C6afyWDsRiPch3FB5Inw.sApD6QjRXa.TR9osrkcjXgT.vfSFzdO"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "rojowt"
                password "$2y$10$fKI7fwJhb83j1vdd7.S0E.SXW6GZhVB.ctznRvADKxyPL56Fm69De"
                access console 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "saadawya"
                password "$2y$10$tvJtmL6.p4ZKHQUz6Memc.n28mBgDsWiT8pCpk2b.HDkzLWoOkep."
                access console ftp 
                console
                    new-password-at-login
                    member "VF-NSU"
                    member "default"
                exit
            exit
            user "sachin.ip"
                password "$2y$10$P9D9IOxlNKJWDiL2VAvrY.2YwVk6llAqXiFWfanCZZ645BEf.mr7C"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "saik"
                password "$2y$10$rQvDaPBNXktFuRYYH19MA.zOtwdp9AOAkV5xc1wVnXKG/JkA79igy"
                access console ftp 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "sajeert"
                password "$2y$10$/WnqbaI8G3/5y2/1Kd8.A.y7vwAnDvwgCCW.SqUrcfuRKfqLvPjnO"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "samcli"
                password "$2y$10$EXyam8YJMAppUwe5wcRMw.KcdS8bdyV5xGmwmQ7FjQm4/2BUEu1Cm"
                access console 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "sandeep.lamba"
                password "$2y$10$fyDdxCwelPF4fmzLs3l5c.SKSpCJkrYiJlt5pix73YCTth5vIlv.y"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "sandi.ets"
                password "$2y$10$GAsfSQzrByqNtZXee5okU.9Z5QEY5cBL8WcyaMyxl0AnyDV.kkDJK"
                access console ftp 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "santosh.nokia"
                password "$2y$10$n0aJJAXgGrIuMlCWr6uOU.a7DK9qKCNDkNUL8msggRvWnyodTDCty"
                access console 
                console
                    member "default"
                    member "Operator"
                exit
            exit
            user "scp_user"
                password "$2y$10$GyUElJbJh7YVq14mseanM.rp2K2jb/EyoVwvREmQofoz19c3/p//K"
                access console ftp 
                console
                    cannot-change-password
                exit
            exit
            user "semih.ent"
                password "$2y$10$OxWjWcS7T1tSWQra7EPTM.fWsdImRgKpCCKuN88KV4nrRbPi8aNe6"
                access console 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "senem.akpunar"
                password "$2y$10$b2DBHZArHWheIdwz/YqZg.axmvte.lTxwvRD8RMhsyrDgHrTvUiNm"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "sgopal"
                password "$2y$10$oIYzKJRAXS9v98w0gV5fM.CEP1aG9i/izszmbDLbSBlD8DP3kAkvW"
                access console 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "shadi.ets"
                password "$2y$10$wkgks9YCeoidqGIcW6eDo.eBfEs5r7Z1e3kho83KWjD1CHsZ9IMD6"
                access console ftp 
                console
                    member "default"
                    member "SOC"
                exit
            exit
            user "shamidb"
                password "$2y$10$PfnHulxVSi7MmvrUj2hQ..WmeYRfp1XgdU2CuBJ4jDSJNhtuOWmlO"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "sherif"
                password "$2y$10$6.x1E4FJWq4M6ZpBdcjMY.457T81DbFE62mtc0PCuHHaSQ7tOesV6"
                access console ftp 
                console
                    no member "default"
                    member "administrative"
                exit
            exit
            user "sherifg"
                password "$2y$10$ejwFUeWESIqXoILC.HPrw.uky0YjrI.Nl27YVk/qSbWP9P4ofIJoq"
                access console ftp 
                console
                    new-password-at-login
                    no member "default"
                    member "show"
                exit
            exit
            user "sivak"
                password "$2y$10$C12zfwYTbzDEAbf4BdPUc.bAhA8a3ZQly7I4sBzK2y4za68oeeiuO"
                access console ftp 
                console
                    new-password-at-login
                    member "administrative"
                    member "default"
                exit
            exit
            user "snmpv3user"
                password "$2y$10$cWGykUsuM7/2cMzOg8VRk.PlRtYfu8PUs.TAFg5LtaNdOVDJMp00a"
                access snmp 
                snmp
                    authentication hash sha 7218309be391e7b19c30e30a28bdf9770f2388e4db55ab4c privacy des-key 7218309be391e7b19c30e30a28bdf977
                    group "nmsPriv"
                exit
            exit
            user "srinivasalu"
                password "$2y$10$fc/dMYM0uVpceMiWIbc86.JOzzj8MhAK/iB5URbi9/dHPgc5jxMsW"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "subheep"
                password "$2y$10$OMkOondtIqRkw/s6nXtVM.GIIFapMpqNhI.Oj736L87nDrT5vY6oK"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "sudhanshu"
                password "$2y$10$YZ5yR4ZcE2qsoG6o/ZVXQ.vvkQ3LKkM/lz5jESysbcs4sDL2Vnwzq"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "sujith"
                password "$2y$10$TsWR4wD/AGAqlxDrwrOzs.q.ijW.UHVE..W/6HoqRBoUUuplHvvjS"
                access console ftp 
                console
                    member "administrative"
                    member "default"
                exit
            exit
            user "svenkat"
                password "$2y$10$xjSPCU4rVOnNbSiMDFeY6.0.EMB1l./RsH3XhxVhWsRGpeg1gYBd."
                access console 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "syeda"
                password "$2y$10$7xfLGrQbiirOuAQx7XaSk.WHA.puw1fgxOK7T7M8CpUGO3/8klZOG"
                access console ftp 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "test"
                password "$2y$10$/YyEng1xioFO28DdwS4Ys.5Pi5nJWj4Ffh8eJ1O3i8ha/mQWwTvPK"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vfq.mali"
                password "$2y$10$OgC0yyN8mG9IDgYaENvu..zYt7al0gQcMTIi.J9V6FpgO9FCm6qfu"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vijay.singh"
                password "$2y$10$zfHIAwXK2KiCqAs8QZum6.faSYVsfLpU8rzyXeq6vAstsK6.y8KWu"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "vinodk"
                password "$2y$10$G712VrbUEuDqdhCchWmP2.dCOWwnMiXvruUd0M9DhiGuy4nWhh2DC"
                access console ftp 
                console
                    new-password-at-login
                    no member "default"
                    member "administrative"
                exit
            exit
            user "vishaldeep"
                password "$2y$10$BzC250Jxr6toYGecdz35o.AOUWcpDSQJokujF1bcYnzFwhaS6ixzW"
                access console ftp 
                console
                    new-password-at-login
                    member "default"
                    member "administrative"
                exit
            exit
            user "vivekk"
                password "$2y$10$wyA.4IpBIk00hqgCIXECc.X9i1Ia41vqmPfv4/lkgdr3hXjRhMYiu"
                access console ftp 
                console
                    new-password-at-login
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "vkumar"
                password "$2y$10$6zn/hhdJGC8P3vyeJC6KY.vSjB47bMAmPfpVvFM1cIDYu9DshZLUu"
                access console 
                console
                    member "default"
                    member "VF-NSU"
                exit
            exit
            user "wslomins"
                password "$2y$10$d.y/52/4KZ93hW4eVF2g2.udnTtyAGyUqC.AbkdTdQq8gLrHMV3gq"
                access console ftp 
                console
                    member "default"
                    member "administrative"
                exit
            exit
            user "yousef"
                password "$2y$10$tlqUmHjknDAdIkj996mlY.xWBIyJZg1WCc0qFCINcyCojBAqU8c3O"
                access console ftp 
                console
                    member "default"
                    member "Monitoring"
                exit
            exit
            user "zeliha"
                password "$2y$10$sCPbRfS1YEAz6DOEDIPXE.pMWDKSemLtfbsv4k8C2pQeu7vaMkpeW"
                access console ftp 
                console
                    member "default"
                    member "ARCH2"
                exit
            exit
            snmp
                access group "nmsPriv" security-model usm security-level privacy read "iso" write "iso" notify "iso"
                access group "nmsPriv" security-model usm security-level privacy context "vprn" prefix read "vprn-view" write "vprn-view" notify "iso"
                access group "nmsNoAuth" security-model usm security-level no-auth-no-privacy read "iso" write "iso" notify "iso"
                community "toTlp9V2fM4Xlk/6J5lSuWaBLCnT" hash2 r version v2c
                community "cV3ISTw2V5pbEWmVEA9jXgB/1EERXQA=" hash2 rwa version v2c
            exit
            ssh
                preserve-key
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
        vprn 55000 customer 1 create
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
            service-name "ENT-4G-5G_Public"
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
