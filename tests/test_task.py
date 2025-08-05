import pytest


@pytest.mark.parametrize(
    "priority_level",
    [1, 2, 3, 4],
    ids=[
        "Create task with Priority 1",
        "Create task with Priority 2",
        "Create task with Priority 3",
        "Create task with Priority 4",
    ],
)
def test_add_task_with_priority(add_task_page, priority_level):
    page = add_task_page

    page.create_task(priority_level, page.title)
    assert page.assert_task_priority(priority_level)
