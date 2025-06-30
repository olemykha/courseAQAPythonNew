from homework.homework16.task1.rhombus_inheritance import TeamLead


def test_teamlead_inherits_all_attributes():
    tl = TeamLead(
        name="Alex",
        salary=3000.0,
        department="QA Engineering",
        programming_language="Python",
        team_size=5
    )

    assert hasattr(tl, "name")
    assert tl.name == "Alex"
    assert hasattr(tl, "salary")
    assert tl.salary == 3000.0

    assert hasattr(tl, "department")
    assert tl.department == "QA Engineering"

    assert hasattr(tl, "programming_language")
    assert tl.programming_language == "Python"

    assert hasattr(tl, "team_size")
    assert tl.team_size == 5
