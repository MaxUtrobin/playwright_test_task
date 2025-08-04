import pytest


@pytest.mark.parametrize(
    "priority_level",
    [1, 2, 3, 4],
    ids=[
        "Create task with Priority 1",
        "Create task with Priority 2",
        "Create task with Priority 3",
        "Create task with Priority 4"
    ]
)
def test_add_task_with_priority(add_task_page, priority_level):
    page = add_task_page

    page.click_add_task()
    page.add_task_title()
    page.add_task_description()
    page.add_task_priority(priority_level)
    page.save_task()
    page.select_task(page.task_title_obj)

    assert page.assert_task_priority(priority_level)
