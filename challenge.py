import yaml

DISQUALIFICATION_THRESHOLD = 7


def average_without_extremes(scores):
    sorted_scores = sorted(scores)
    # For each user toss out min/max scores
    # Calculate averages
    return sum(sorted_scores[1:-1]) / (len(scores) - 2)


def main():
    disqualified = []
    # Note: we could use a better data structure to maintain a top 3, but it's not necessary.
    winners = {}
    best_scores = [0, 0, 0]  # So we can keep the top 3.
    worst_best_score = 0

    # Process scores file
    with open('scores.yaml') as file:
        people = yaml.load(file, Loader=yaml.FullLoader)

        for person, scores in people.items():
            # Ignore anybody without DISQUALIFICATION_THRESHOLD scores
            if len(scores) < DISQUALIFICATION_THRESHOLD:
                disqualified.append(person)
                continue

            average = average_without_extremes(scores)

            # Keep the top 3.
            if average > worst_best_score:
                winners.pop(worst_best_score, None)
                winners[average] = person
                best_scores.remove(worst_best_score)
                best_scores.append(average)
                worst_best_score = sorted(best_scores)[0]

    # write result file (e.g.)
    # winners:
    # - name: Cal Ripken
    #   avg: 76.3333333
    # - name: Boy George
    #   avg: 73.2
    # - name: Dwight Schrute
    #   avg: 70
    # disqualifications:
    # - Dougie Fresh
    # - Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr.
    with open('results.yaml', 'w') as file:
        data = {}
        data['winners'] = []
        print(best_scores)
        print(winners.keys())

        for score in sorted(best_scores, reverse=True):
            data['winners'].append({'name': winners[score], 'avg': score})
        data['disqualifications'] = disqualified
        yaml.safe_dump(data, file, sort_keys=False, explicit_start=True)


# Note: for production readiness, I would have added more tests, and broken this down into smaller functions.

if __name__ == '__main__':
    main()