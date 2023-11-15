courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]

durations = [14, 20, 12, 20]

def get_unique_name():

    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.partition(' ')[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)
    all_names_sorted = sorted(unique_names)
    all_names_sorted = ', '.join(all_names_sorted)
    return all_names_sorted


def get_course(durations):
    courses_list = []

    for course, course_mentors, duration in zip(courses, mentors, durations):
        course_dict = {'title':course, 'course_mentors':course_mentors, 'duration':duration}
        courses_list.append(course_dict)

    min_value = min(durations)
    max_value = max(durations)

    maxes = []
    minis = []
    for index, value in enumerate(durations):
        if value == max_value:
            maxes.append(index)
        elif value == min_value:
            minis.append(index)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['title'])
    
    for id in maxes:
        courses_max.append(courses_list[id]['title'])
    
    return f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_value} месяца(ев)\nСамый длинный курс(ы): {", ".join(courses_max)} - {max_value} месяца(ев)'

def get_top_names(mentors):
    all_list_names = []
    [all_list_names.extend(names) for names in mentors]

    i = 0
    for name in all_list_names:
        all_list_names[i] = name.partition(' ')[0]
        i += 1

    uniques_names = set(all_list_names)
    uniques_names = sorted(uniques_names)

    popular = []
    for name in uniques_names:
        popular.append([name, all_list_names.count(name)])

    popular.sort(key=lambda x:x[1], reverse=True)

    top_3 = popular[:3]

    top_3_str = ''
    for name, count in top_3:
        top_3_str += f'{name}: {count} раз(а), '

    return top_3_str.strip(', ')
