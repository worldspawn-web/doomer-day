﻿# Characters:
define doomer = Character('Думер', color="#6655fa")


# Scenario:
label start:

    "Я снова здесь..."

    "Снова в этой бескрайней мгле..."

    "Снова рассуждаю о смысле своего жалкого бытия..."

    "В чём смысл нашей жизни?"

    "Мы рождаемся, хотя об этом никогда и не просили..."

    "Проживаем эту жизнь, плодим потомство, умираем."

    "И так каждый раз. Снова и снова. Поколение за поколением."

    "Бесконечный бессмысленный цикл."

    "...или смысл в этом цикле всё-таки есть?"

    play sound "phone_alarm.mp3"

    pause 5

    scene bg ceiling_1
    with Dissolve(.5)
    pause 1

    doomer "Ещё... 5 минуточек..."

    # TODO: replace with empty black background
    scene
    with Dissolve(2)

    stop sound fadeout 3
    pause 3.3

    "А для чего жили наши родители?"

    "Вот допустим, мой отец всю жизнь проработал на заводе за копейки. Каждый рабочий день он вставал в 6 часов утра, громко гремел чашками на кухне и кипятил чайник."

    "Каждое утро он начинал с омлета, попутно слушая неизвестное мне радио, где обсуждали всё на свете, но только не полезные вещи."

    "А кто-то сейчас вообще радио слушает?"

    "Отец начинал каждое утро именно так. Отличий практически не было. Уверен, что на работе всё было по той же тенденции."

    "Это же настоящий День Сурка!"

    "Какой смысл в повторении одного и того же действия? День за днём, год за годом."

    "Хотя, чем я отличаюсь от него?"

    play sound "phone_alarm.mp3"

    pause 5

    scene bg ceiling_1
    with Dissolve(.5)
    pause 1

    "Вставать мне совершенно не хотелось. Однако выбора у меня не было."
    
    "Работа не ждёт."

    "Нужно платить за квартиру и хоть чем-то питаться до следующей выплаты."

    stop sound

    "Иронично."

    # TODO: add bathroom mirror scene
    # scene bg bathroom_dark_dirty
    # with Dissolve(.5)
    # pause 1

    "В ванной было как всегда жутковато мрачно."

    doomer "Точно. Лампочка. Снова забыл."

    "Вот уже как полгода я 'забываю' купить лампочку, по дороге домой."

    "Но на самом деле, после работы у меня нет сил думать о чём-либо, кроме чая, компьютера, звёздном бескрайнем небе."

    "В целом, отсутствие лампочки никак мне не мешает."

    "Хотя бриться стало довольно проблематично. Но делаю это я раз в месяц, может в полтора."

    "Борода у меня растёт не быстро."

    # play sound "bathrrom_tap_water_on.mp3"
    pause 5
    # play sound "bathroom_tap_water_off.mp3"

    # scene bg bathroom_dark_fresh
    # with Dissolve(.5)
    # pause 2

    doomer "Совсем другое дело."

    "На самом деле, ничего толком не изменилось, но стало проще моргать."

    "Свежесть даёт о себе знать."

    "Сложно было назвать это умыванием. Я плескал воду себе на лицу без какой-либо цели."

    "Так было проще проснуться, но какой-то особой чистоты это не придавало."

    # scene bg kitchen_morning
    # with Dissolve(.5)
    # pause 1

    "Неизменный утренний вид из окна, каждый раз вдохновлял меня."

    "Но мне не хватало сил осознать на что именно."

    "Было в утреннем времени что-то такое..."

    "Особенное?"

    "Будто бы мир на эти несколько часов становился совершенно иным. Непохожим на день или вечер."

    "Ночь была близка к этому состоянию, но придавала совершенно другие эмоции."

    # TODO: re-do with possible png pic, not the whole scene? + diff. naming
    # scene bg kitchen_morning_boiling_water
    # with Dissolve(.5)
    # pause 1

    # maybe extend this philosophical idea with more deep depressive lyrics
    "Ночью хотелось потеряться. Забыться навсегда в этой утопии серых стен." 

    "Нет. Утреннее ощущение совсем не похоже. Всё же они настолько же далеки, насколько близки."

    return
