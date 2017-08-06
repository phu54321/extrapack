extern array euda_cursnl, pndb_arr

function bgmloop()
    if istimerhit() then
        starttimer(70373)
        inline for player = 0, 7 do
            SetCurrentPlayer(player)
            PlayWAV('staredit\\wav\\bgmmain.wav')
        end
    end
end

function getstringaddr(strid)
    var strsection_addr = dwread_epd(EPD(0x5993D4))
    var stroffset = wread(strsection_addr + 2 * strid)
    return strsection_addr + stroffset
end

function delay(framen)
    for i = 1, framen do
        RemoveUnit("Zerg Larva", Force1)
        SetMemory(0x6509A0, SetTo, 0)
        DoEvents()
    end
end


inline function applyeudpatch()
    -- Basic eud patch
    SetMemory(0x6617C8 + 120 * 8 + 0, SetTo, 0x001F001F)
    SetMemory(0x6617C8 + 120 * 8 + 4, SetTo, 0x001F001F)

    -- 다크아콘
    SetMemory(0x6617C8 + 63 * 8 + 0, SetTo, 0x00140014)
    SetMemory(0x6617C8 + 63 * 8 + 4, SetTo, 0x00130013)

    -- 아콘
    SetMemory(0x6617C8 + 68 * 8 + 0, SetTo, 0x00140014)
    SetMemory(0x6617C8 + 68 * 8 + 4, SetTo, 0x00130013)

    -- 스카웃
    -- 12 00 11 00 11 00 10 00
    SetMemory(0x6617C8 + 70 * 8 + 0, SetTo, 0x00120012)  -- 그냥
    SetMemory(0x6617C8 + 70 * 8 + 4, SetTo, 0x00110011)
    SetMemory(0x6617C8 + 80 * 8 + 0, SetTo, 0x00120012)  -- mojo
    SetMemory(0x6617C8 + 80 * 8 + 4, SetTo, 0x00110011)
    SetMemory(0x6617C8 + 88 * 8 + 0, SetTo, 0x00120012)  -- Artanis
    SetMemory(0x6617C8 + 88 * 8 + 4, SetTo, 0x00110011)

    -- Make units unclickable
    SetMemory(0x66C150 + 292, SetTo, 0x00000001)  -- Machine shop
    SetMemory(0x66C150 + 188, SetTo, 0x00000000)  -- Pylon
    SetMemory(0x66C150 + 140, SetTo, 0x00000000)  -- Scout & Heros
    SetMemory(0x66C150 + 242, SetTo, 0x00000000)  -- Wraith & Heros
    SetMemory(0x66C150 + 24, SetTo, 0x00000000)  -- Guardian
    SetMemory(0x66C150 + 936, SetTo, 0x00000101)  -- Valkyrie
    SetMemory(0x66C150 + 216, SetTo, 0x00000101)  -- Battlecruiser
    SetMemory(0x66C150 + 132, SetTo, 0x00000000)  -- Archon
    SetMemory(0x66C150 + 924, SetTo, 0x00000000)  -- Dark Archon
    SetMemory(0x66C150 + 42, SetTo, 0x00000000)  -- Overlord
    SetMemory(0x66C150 + 16, SetTo, 0x00000000)  -- Drone

    -- Set turn radius to minimal (1)
    -- 6C9E20 : Flingy.dat - turn radius
    SetMemory(0x6C9E20 + 0, SetTo, 0x00281B7F)  -- Scourge (0) -> 127
    SetMemory(0x6C9E20 + 4, SetTo, 0x2800281B)  -- Guardian (7)
    SetMemory(0x6C9E20 + 40, SetTo, 0x28282828)  -- Scout (43)
    SetMemory(0x6C9E20 + 80, SetTo, 0x0D0D2828)  -- Wraith (80)
    SetMemory(0x6C9E20 + 188, SetTo, 0x282828)  -- Valkyrie & Corsair
    SetMemory(0x6C9E20 + 68, SetTo, 0x28280000)  -- Battlecruiser (70)
end


function main()
    initextstr()
    applyeudpatch()

    -- Prohibit single play
    if Memory(0x57F0B4, Exactly, 0) then
        inline for player = 0, 7 do
            SetCurrentPlayer(player)
            DisplayText('\x05싱글플레이를 하실 수 없습니다.')
            Draw()
        end

        delay(-1)
    end

    inline for player = 0, 7 do
        SetCurrentPlayer(player)
        DisplayExtText(SCMD2Text(
            '<13><0F><04>Missile pack <02>[Extra]<04>\n'
            '\n'
            '<13><05>Created by cpy3001\n'
            '\n'))
    end

    for i = 1, 3000 / 48 do
        CenterView('Anywhere')
        SetMemory(0x6509A0, SetTo, 0)
        DoEvents()
    end

    -- Get checkcodes
    var initialstage, difficulty, tryn
    
    inline if not config.debugmode then
        difficulty, initialstage, tryn = checkcode()
    inline else
        difficulty = config.difficulty
        initialstage = config.initialstage
        tryn = 0
        RemoveUnitAt(All, '(any unit)', 'lvselbox', AllPlayers)
    end


    var proceeded_flag = 0
    var saven_strid = EncodeString('\x04라이프 \x03| \x04세이브 횟수 : 00번 이상')
    var soffset = getstringaddr(saven_strid)
    soffset = dbstr_print(offset, '\x04라이프 \x03| \x04세이브 횟수 : ', tryn)
    if tryn == 20 then
        soffset = dbstr_print(soffset, '번 이상')
    end

    -- Init bgm loop
    f_starttimer(19232)
    inline for player = 0, 5 do
        SetCurrentPlayer(player)
        PlayWAV('staredit\\wav\\bgmstart.wav')
        RunAIScript('Turn ON Shared Vision for Player 8')
    end

    SetDeaths(P8, SetTo, initialstage - 1, "@PatternSelector")
    SetDeaths(P8, SetTo, difficulty, "@Difficulty")
    SetDeaths(P8, SetTo, 2, "@GameState")
    SetResources(Force1, SetTo, 25, Gas)  -- 초기 라이프 30개 (25 + 5)
    LeaderBoardResources(Gas, saven_strid)
    LeaderBoardComputerPlayers(Disable)
    SetMemory(0x51CE98, SetTo, 2)  -- 터보시야
    SetMemory(0x6509A0, SetTo, 1)

    DoEvents()

    -- Repulse map handle : 공중유닛끼리 밀림 현상 방지용
    var reph_epd = epdread_epd(EPD(0x6D5CD8))
    var userpl = getuserplayerid()

    while True do
        bgmloop()
        RunTrigTrigger()

        -- 코드 계산
        if Deaths(P8, Exactly, 4, '@GameState') then -- 패배 처리
            losetext()
            inline for pl = 0, 5 do
                SetCurrentPlayer(pl)
                Defeat()
            end
            delay(-1)
        
        elseif Deaths(P8, Exactly, 5, '@GameState') then -- 승리 처리
            victorytext()
            inline for pl = 0, 5 do
                SetCurrentPlayer(pl)
                SetAllianceStatus(Force1, AlliedVictory)
            end

            inline for pl = 0, 5 do
                Victory()
            end
            delay(-1)

        end

        -- 코드 재계산이 필요하다.
        if Switch('UpdateStageCode', Set):
            -- 재시도 횟수 업데이트.
            if proceeded_flag == 0 then
                proceeded_flag = 1
            elseif proceeded_flag == 1 then
                proceeded_flag = 2
                tryn = tryn + 1
                if tryn == 21 then
                    tryn = 20
                end
            end

            -- 재계산
            stage = dwread_epd(12 * EncodeUnit('@PatternSelector') + 7) - 1
            difficulty = dwread_epd(12 * EncodeUnit('@Bifficulty') + 7)
            code = gethash(userpl, difficulty, stage, tryn)

            if stage ~= euda_cursnl[difficulty]) then  -- 막탄 아닌 경우
                -- 스트링 변형
                local target_strid = EncodeString('#' * 512)
                local soffset = getstringaddr(target_strid)

                soffset = dbstr_print(soffset, '\x13\x02')

                if difficulty == 0 then
                    soffset = dbstr_print(soffset, 'Easy ')
                elseif difficulty == 1 then
                    soffset = dbstr_print(soffset, 'Normal ')
                elseif difficulty == 2 then
                    soffset = dbstr_print(soffset, 'Hard ')
                end

                soffset = dbstr_print(soffset, stage + 1, ''' : \x04''')
                soffset = dbstr_addstr(
                    soffset,
                    pndb_arr[config.diffn * stage + difficulty]
                )
                soffset = dbstr_print(soffset, '\n\x13\x05세이브 코드 : 000000')

                if stage == 0 then
                    dbstr_print(soffset - 6, '없음')
                else
                    writebase24str(code, soffset - 6)
                end

                -- 텍스트 출력
                inline for pl = 0, 5 do
                    SetCurrentPlayer(pl)
                    DisplayText(target_strid)
                    SetMissionObjectives(target_strid)
                end
            end

            SetSwitch('UpdateStageCode', Clear)
        end

        -- 통과속성 다시 활성화
        unitptr, unitepd = dwepdread_epd(EPD(0x628430))
        while unitptr ~= 0 do
            -- 통과속성 적용 안할 유닛들 제외
            unitType = f_dwread_epd(unitepd + 0x64 / 4)
            if not (
                unitType == EncodeUnit('Block') or
                unitType == EncodeUnit('Bunker') or
                unitType == EncodeUnit('Dodger')
            ) then
                -- statusFlag 설정
                local statusFlag = dwread_epd(unitepd + 0xDC / 4) | 0x200000
                dwwrite_epd(unitepd + 0xDC / 4, statusFlag)

                -- 멈춤 설정
                local playerID = f_dwbreak(f_dwread_epd(unitepd + 0x4C / 4))[2]
                if (
                    (Switch('LockMissileP7', Set) and playerID == 6) or
                    (Switch('LockMissileP8', Set) and playerID == 7)
                ) then
                    SetDeaths(unitepd + 0x38 / 4, SetTo, 0, 0)
                    SetDeaths(unitepd + 0x3C / 4, SetTo, 0, 0)
                    SetDeaths(unitepd + 0x40 / 4, SetTo, 0, 0)
                    SetDeaths(unitepd + 0x44 / 4, SetTo, 0, 0)
                end
            end

            unitptr, unitepd = dwepdread_epd(unitepd + 1)
        end

        -- Repulse Map를 계속 0으로 설정 -> 공중유닛끼리 밀림 현상 방지
        dwmemset_epd(reph_epd, 0, 29244 / 4)
        
        -- 락다운 처리
        if Switch('LockDrone', Set) then
            inline for player = 0, 5 do
                 if Bring(player, AtLeast, 1, 'Dodger', 'ground') then
                    MoveLocation('ptrace', 'Dodger', player, 'Anywhere')
                    CreateUnit(1, 'Kakaru', 'ptrace', P8)
                    KillUnitAt(All, 'Kakaru', 'ptrace', P8)
                    MoveUnit(All, 'Dodger', player, 'ptrace', 'ptrace')
                end
            end
            KillUnit('Kakaru', P8)
        end

        SetMemory(0x6509A0, SetTo, 0)  -- EUD Turbo trigger
        DoEvents()
    end
end



------------
--
--  Game ending
--
------------

function dptext(text -> EncodeString)
    SetCurrentPlayer(userpl)
    DisplayText(text)
end


function losetext()
    for i = 1, 2 do
        SetCurrentPlayer(userpl)
        DisplayText('\x13\x08^^^^^^^^^^ 마지막 탄 정보 ^^^^^^^^^^'),
        DisplayText('#' * 512),  -- 패턴 정보 등등
        DisplayText('\x13\x08^^^^^^^^^^ 마지막 탄 정보 ^^^^^^^^^^'),
        delay(24 * 3)
    end

    dptext('\n' * 13)
end

function victorytext()
    dptext(SCMD2Text('''\
<13><1E>====================================
<13><02>Final Stage : <04>엔딩
<13><05>세이브 코드 : ??????
<13><1E>===================================='''))
    delay(24 * 4)

    dptext(SCMD2Text('''\








<13><1E>====================================
<13><02>제작 계기/방향
<13><04>eudplib/trggen 데모맵
<13><04>미사일팩의 장르화 연구
<13><1E>===================================='''))

    delay(24 * 5)

    dptext(SCMD2Text('''\







<13><1E>====================================    　
<13><02>아이디어를 얻은 맵들
<13><04>Level up bound
<13><04>Extreme pack 1.xG
<13><04>미사일피하기 MsPack
<13><1E>===================================='''))

    delay(24 * 5)

    dptext(SCMD2Text('''\




<13><1E>====================================
<13><02>Special Thanks To
<13><04>Qwe  Lead  Love  Eud[fx]
<13><04>rhwkplayer1  Uin`

<13><04>http:/cafe.naver.com/missilewarfare
<13><1E>===================================='''))

    delay(24 * 5)

    dptext(SCMD2Text('''\






<13><1E>====================================
<13><04>플레이해주셔서 감사합니다.

<13>ㄴㅓㅈㅣㅎㅏ
<13>ㄷㅃㅓㅅㄴ
<13>ㅗㄹㄷㅏ

<13><04>개발기간 : 2014.02.24 ~ 2015.07.15
<13><1E>===================================='''))

    delay(24 * 5)
end
