import 'package:flutter_test/flutter_test.dart';
import 'package:evalon/main.dart';

void main() {
  testWidgets('Evalon app smoke test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const EvalonApp());

    // Verify splash screen shows
    expect(find.text('EVALON'), findsOneWidget);
  });
}
