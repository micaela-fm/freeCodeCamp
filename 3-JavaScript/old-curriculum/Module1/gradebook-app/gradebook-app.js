const getAverage = scores => scores.reduce((sum, score) => sum + score, 0) / scores.length;

const getGrade = score => {
  if (score === 100) return "A++";
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
};

const hasPassingGrade = score => getGrade(score) !== "F";

const studentMsg = (totalScores, studentScore) => {
  const average = getAverage(totalScores);
  const grade = getGrade(studentScore);
  const passingMsg = hasPassingGrade(studentScore) ? "You passed the course." : "You failed the course.";
  return `Class average: ${average.toFixed(2)}. Your grade: ${grade}. ${passingMsg}`;
};

console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));
