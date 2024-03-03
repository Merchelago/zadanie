from .models import Product, Group, User


def distribute_user_to_group(product, user):
    groups = Group.objects.filter(product=product).order_by('min_users', 'max_users')
    user_count = User.objects.count()
    for group in groups:
        if group.is_full():
            continue
        group.user_set.add(user)
        return group
    # Если все группы заполнены, создаем новую группу
    new_group = Group.objects.create(product=product, name=f"Group {len(groups) + 1}",
                                      min_users=1, max_users=10)  # Пример значений минимального и максимального количества участников
    new_group.user_set.add(user)
    return new_group